from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState


class DummyAgent(BaseAgent):

    def run(self, state: LeadPilotState) -> LeadPilotState:

        print("Dummy Agent Executed")

        state.company.company_name = "OpenAI"
        state.company.website = "https://openai.com"

        return state