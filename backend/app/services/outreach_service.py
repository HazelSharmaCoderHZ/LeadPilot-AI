from app.schemas.state import LeadPilotState
from app.services.providers.llm.base import BaseLLM


class OutreachService:

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def generate_email(self, state: LeadPilotState):

        contact = (
            state.contacts[0]
            if state.contacts
            else None
        )

        result = self.llm.generate_outreach_email(
            company_name=state.company.company_name or "",
            industry=state.company.industry or "",
            summary=state.analysis.summary or "",
            pain_points=state.analysis.pain_points,
            contact_name=contact.name if contact else "",
            contact_role=contact.role if contact else "",
        )

        return result
