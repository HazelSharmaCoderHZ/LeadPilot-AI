from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState


class SuccessAgent(BaseAgent):

    def run(self, state: LeadPilotState) -> LeadPilotState:
        state.company.name = "OpenAI"
        return state


def test_execute_success():

    state = LeadPilotState()

    agent = SuccessAgent()

    result = agent.execute(state)

    assert result.company.name == "OpenAI"