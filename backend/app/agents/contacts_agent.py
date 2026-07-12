from app.agents.base import BaseAgent
from app.schemas.state import ContactState, LeadPilotState
from app.services.contacts_service import ContactsService


class ContactsAgent(BaseAgent):

    def __init__(self, service: ContactsService):
        super().__init__()
        self.service = service

    def run(self, state: LeadPilotState) -> LeadPilotState:

        contacts = self.service.find_contacts(
            state.company.company_name,
            state.company.website,
        )

        state.contacts = [
            ContactState(
                name=contact.name,
                role=contact.role,
                email=contact.email,
                linkedin=contact.linkedin,
            )
            for contact in contacts
        ]

        return state
