from langgraph.graph import START, END, StateGraph

from app.schemas.state import LeadPilotState
from app.agents.reviewer import ReviewerAgent
from app.agents.research_agent import ResearchAgent
from app.agents.analysis_agent import AnalysisAgent
from app.agents.contacts_agent import ContactsAgent
from app.agents.qualification_agent import QualificationAgent
from app.agents.outreach import OutreachAgent

builder = StateGraph(LeadPilotState)

research_agent = ResearchAgent()
analysis_agent = AnalysisAgent()
contacts_agent = ContactsAgent()
qualification_agent = QualificationAgent()
outreach_agent = OutreachAgent()
reviewer_agent = ReviewerAgent()

builder.add_node("research", research_agent.execute)
builder.add_node("analysis", analysis_agent.execute)
builder.add_node("contacts", contacts_agent.execute)
builder.add_node("qualification", qualification_agent.execute)
builder.add_node("outreach", outreach_agent.execute)
builder.add_node("reviewer", reviewer_agent.execute)

builder.add_edge(START, "research")
builder.add_edge("research", "analysis")
builder.add_edge("analysis", "contacts")
builder.add_edge("contacts", "qualification")
builder.add_edge(
    "qualification",
    "outreach",
)

builder.add_edge(
    "outreach",
    "reviewer",
)

builder.add_edge(
    "reviewer",
    END,
)
lead_pipeline = builder.compile()