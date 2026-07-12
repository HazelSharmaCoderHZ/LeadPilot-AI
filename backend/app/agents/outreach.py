from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState
from app.services.outreach_service import OutreachService


class OutreachAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.service = OutreachService()

    def run(self, state: LeadPilotState):

        result = self.service.generate_email(state)

        state.outreach.subject = result.subject
        state.outreach.body = result.body
        state.outreach.cta = result.cta
        state.outreach.personalization_summary = (
            result.personalization_summary
        )

        return state