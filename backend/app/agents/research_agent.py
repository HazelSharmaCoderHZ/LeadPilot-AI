from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState

from app.services.providers.crawlers.firecrawl import FirecrawlCrawler
from app.services.research_service import ResearchService


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.service = ResearchService(FirecrawlCrawler())

    def run(self, state: LeadPilotState) -> LeadPilotState:
        if not state.company.website:
            raise ValueError("Website is required.")
        result = self.service.research(state.company.website)

        # Populate ResearchState
        state.research.company_name = result.company_name
        state.research.title = result.title
        state.research.description = result.description
        state.research.summary = result.summary
        state.research.language = result.language

        # Populate ScrapedContentState
        state.scraped_content.website = result.website
        state.scraped_content.markdown = result.raw_markdown
        state.scraped_content.metadata = result.metadata

        return state