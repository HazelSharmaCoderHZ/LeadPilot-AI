from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState, WorkflowStatus


class SuccessAgent(BaseAgent):

    def run(self, state: LeadPilotState) -> LeadPilotState:
        state.company.company_name = "OpenAI"
        return state


class FailingAgent(BaseAgent):

    def run(self, state: LeadPilotState) -> LeadPilotState:
        raise RuntimeError("provider unavailable")


def test_execute_success():

    state = LeadPilotState()

    agent = SuccessAgent()

    result = agent.execute(state)

    assert result.company.company_name == "OpenAI"
    assert result.execution.status is WorkflowStatus.COMPLETED


def test_execute_failure_records_error_and_failed_status():
    result = FailingAgent().execute(LeadPilotState())

    assert result.execution.status is WorkflowStatus.FAILED
    assert result.execution.current_agent == "FailingAgent"
    assert result.execution.errors == ["provider unavailable"]


def test_execute_does_not_overwrite_an_existing_failure():
    state = FailingAgent().execute(LeadPilotState())

    result = SuccessAgent().execute(state)

    assert result.execution.status is WorkflowStatus.FAILED
    assert result.execution.current_agent == "FailingAgent"
    assert result.execution.errors == ["provider unavailable"]
    assert result.company.company_name is None
