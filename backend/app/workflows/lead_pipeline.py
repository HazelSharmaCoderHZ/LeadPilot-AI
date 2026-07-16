from langgraph.graph import END, START, StateGraph

from app.agents.analysis_agent import AnalysisAgent
from app.agents.contacts_agent import ContactsAgent
from app.agents.outreach import OutreachAgent
from app.agents.qualification_agent import QualificationAgent
from app.agents.research_agent import ResearchAgent
from app.agents.reviewer import ReviewerAgent
from app.schemas.state import LeadPilotState
from app.services.analysis_service import AnalysisService
from app.services.contacts_service import ContactsService
from app.services.outreach_service import OutreachService
from app.services.providers.crawlers.firecrawl import FirecrawlCrawler
from app.services.providers.llm.gemini import GeminiProvider
from app.services.providers.search.tavily import TavilyProvider
from app.services.qualification_service import QualificationService
from app.services.research_service import ResearchService
from app.services.reviewer_service import ReviewerService


def should_continue(state: LeadPilotState) -> str:
    if state.execution.status.value == "failed":
        return "end"
    return "continue"


def build_lead_pipeline(
    research_agent: ResearchAgent,
    analysis_agent: AnalysisAgent,
    contacts_agent: ContactsAgent,
    qualification_agent: QualificationAgent,
    outreach_agent: OutreachAgent,
    reviewer_agent: ReviewerAgent,
):
    builder = StateGraph(LeadPilotState)

    builder.add_node("research", research_agent.execute)
    builder.add_node("analysis", analysis_agent.execute)
    builder.add_node("contacts", contacts_agent.execute)
    builder.add_node("qualification", qualification_agent.execute)
    builder.add_node("outreach", outreach_agent.execute)
    builder.add_node("reviewer", reviewer_agent.execute)

    builder.add_edge(START, "research")
    builder.add_conditional_edges(
        "research",
        should_continue,
        {"continue": "analysis", "end": END},
    )
    builder.add_conditional_edges(
        "analysis",
        should_continue,
        {"continue": "contacts", "end": END},
    )
    builder.add_conditional_edges(
        "contacts",
        should_continue,
        {"continue": "qualification", "end": END},
    )
    builder.add_conditional_edges(
        "qualification",
        should_continue,
        {"continue": "outreach", "end": END},
    )
    builder.add_conditional_edges(
        "outreach",
        should_continue,
        {"continue": "reviewer", "end": END},
    )
    builder.add_edge("reviewer", END)

    return builder.compile()


def build_production_pipeline():
    crawler = FirecrawlCrawler()
    search_provider = TavilyProvider()
    llm = GeminiProvider()

    return build_lead_pipeline(
        research_agent=ResearchAgent(ResearchService(crawler)),
        analysis_agent=AnalysisAgent(AnalysisService(llm)),
        contacts_agent=ContactsAgent(ContactsService(search_provider,llm,)),
        qualification_agent=QualificationAgent(QualificationService(llm)),
        outreach_agent=OutreachAgent(OutreachService(llm)),
        reviewer_agent=ReviewerAgent(ReviewerService(llm)),
    )


lead_pipeline = build_production_pipeline()
