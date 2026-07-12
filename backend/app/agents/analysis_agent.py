from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState
from app.services.analysis_service import AnalysisService


class AnalysisAgent(BaseAgent):

    def __init__(self, service: AnalysisService):
        super().__init__()
        self.service = service

    def run(self, state: LeadPilotState):

        result = self.service.analyze(
            state.scraped_content.markdown
        )

        state.analysis.summary = result.company_description
        state.analysis.business_model = result.business_model
        state.analysis.pain_points = result.pain_points

        state.company.company_name = result.company_name
        state.company.industry = result.industry

        return state
