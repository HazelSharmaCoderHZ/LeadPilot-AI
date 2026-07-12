from app.repositories.workflow_repository import WorkflowRepository
from app.schemas.state import CompanyState, LeadPilotState, WorkflowStatus


class FakeSession:
    def __init__(self):
        self.added = []
        self.committed = False
        self.refreshed = []

    def add(self, value):
        self.added.append(value)

    def commit(self):
        self.committed = True

    def refresh(self, value):
        self.refreshed.append(value)


def test_create_persists_serialized_workflow_state():
    state = LeadPilotState(company=CompanyState(company_name="Example Co", website="https://example.com"))
    state.execution.status = WorkflowStatus.COMPLETED
    state.qualification.score = 91
    session = FakeSession()

    run = WorkflowRepository(session).create(state)

    assert session.added == [run]
    assert session.committed is True
    assert session.refreshed == [run]
    assert run.company_name == "Example Co"
    assert run.website == "https://example.com"
    assert run.status == "completed"
    assert run.qualification_score == 91
    assert run.workflow_data["company"]["company_name"] == "Example Co"


def test_create_persists_failed_workflow_state():
    state = LeadPilotState(company=CompanyState(company_name="Example Co", website="https://example.com"))
    state.execution.status = WorkflowStatus.FAILED
    state.execution.current_agent = "ResearchAgent"
    state.execution.errors.append("Firecrawl unavailable")
    session = FakeSession()

    run = WorkflowRepository(session).create(state)

    assert session.committed is True
    assert run.status == "failed"
    assert run.workflow_data["execution"] == {
        "current_agent": "ResearchAgent",
        "status": "failed",
        "errors": ["Firecrawl unavailable"],
    }
