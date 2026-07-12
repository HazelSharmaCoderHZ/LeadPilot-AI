from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState
from app.services.contacts_service import ContactsService


class ContactsAgent(BaseAgent):

    def __init__(self):
        super().__init__()
        self.service = ContactsService()

    def run(self, state: LeadPilotState):

        contacts = self.service.find_contacts(
            state.company.company_name,
            state.company.website,
        )

        state.contacts = contacts

        return state