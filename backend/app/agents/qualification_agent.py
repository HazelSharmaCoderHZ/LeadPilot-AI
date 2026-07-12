from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState
from app.services.qualification_service import QualificationService


class QualificationAgent(BaseAgent):

    def __init__(self, service: QualificationService):
        super().__init__()
        self.service = service

    def run(self, state: LeadPilotState):

        result = self.service.qualify(
            company_name=state.company.company_name,
            industry=state.company.industry,
            summary=state.analysis.summary,
            contacts_found=len(state.contacts),
        )

        state.qualification.score = result.score
        state.qualification.tier = result.tier
        state.qualification.reasoning = result.reasoning

        return state
