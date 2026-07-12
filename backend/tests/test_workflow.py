import pytest

from app.schemas.analysis import AnalysisResult
from app.schemas.outreach import OutreachResult
from app.schemas.qualification import QualificationResult
from app.schemas.research import ResearchResult
from app.schemas.review import ReviewResult
from app.schemas.contact import ContactResult
from app.schemas.state import CompanyState, ContactState, LeadPilotState, WorkflowStatus
from app.agents.analysis_agent import AnalysisAgent
from app.agents.contacts_agent import ContactsAgent
from app.agents.outreach import OutreachAgent
from app.agents.qualification_agent import QualificationAgent
from app.agents.research_agent import ResearchAgent
from app.agents.reviewer import ReviewerAgent
from app.workflows.lead_pipeline import build_lead_pipeline


class FakeResearchService:
    def research(self, website: str) -> ResearchResult:
        return ResearchResult(
            website=website,
            company_name="Example Co",
            title="Example",
            description="Example company",
            language="en",
            raw_markdown="# Example",
        )


class FakeAnalysisService:
    def analyze(self, markdown: str) -> AnalysisResult:
        assert markdown == "# Example"
        return AnalysisResult(
            company_name="Example Co",
            industry="Software",
            company_description="Example company",
            business_model="SaaS",
            pain_points=["Manual prospecting"],
        )


class FakeContactsService:
    def find_contacts(self, company_name: str, website: str) -> list[ContactResult]:
        return [ContactResult(name="Ada", role="CEO", email="ada@example.com")]


class FakeQualificationService:
    def qualify(self, **_: object) -> QualificationResult:
        return QualificationResult(score=88, tier="A", reasoning="Strong fit")


class FakeOutreachService:
    def generate_email(self, state: LeadPilotState) -> OutreachResult:
        assert isinstance(state.contacts[0], ContactState)
        assert state.contacts[0].role == "CEO"
        return OutreachResult(
            subject="A note for Example Co",
            body="Hello Ada",
            cta="Open to a chat?",
            personalization_summary="References manual prospecting.",
        )


class FakeReviewerService:
    def review_email(self, _: LeadPilotState) -> ReviewResult:
        return ReviewResult(
            approved=True,
            score=95,
            feedback=[],
            revised_subject="A note for Example Co",
            revised_body="Hello Ada",
        )


@pytest.fixture(autouse=True)
def workflow():
    return build_lead_pipeline(
        research_agent=ResearchAgent(FakeResearchService()),
        analysis_agent=AnalysisAgent(FakeAnalysisService()),
        contacts_agent=ContactsAgent(FakeContactsService()),
        qualification_agent=QualificationAgent(FakeQualificationService()),
        outreach_agent=OutreachAgent(FakeOutreachService()),
        reviewer_agent=ReviewerAgent(FakeReviewerService()),
    )


def test_workflow_completes_with_fake_providers(workflow):
    state = LeadPilotState(
        company=CompanyState(
            company_name="Example Co",
            website="https://example.com",
        )
    )

    result = LeadPilotState.model_validate(workflow.invoke(state))

    assert result.execution.status is WorkflowStatus.COMPLETED
    assert result.company.industry == "Software"
    assert result.qualification.score == 88
    assert result.contacts[0].role == "CEO"
    assert result.outreach.subject == "A note for Example Co"
    assert result.review.approved is True


def test_workflow_preserves_failure_status():
    downstream_calls = []

    class FailingResearchService:
        def research(self, website: str) -> ResearchResult:
            raise RuntimeError("Firecrawl unavailable")

    class UnexpectedAnalysisService:
        def analyze(self, markdown: str) -> AnalysisResult:
            downstream_calls.append("analyze")
            raise AssertionError("analyze should not run after research fails")

    failing_workflow = build_lead_pipeline(
        research_agent=ResearchAgent(FailingResearchService()),
        analysis_agent=AnalysisAgent(UnexpectedAnalysisService()),
        contacts_agent=ContactsAgent(FakeContactsService()),
        qualification_agent=QualificationAgent(FakeQualificationService()),
        outreach_agent=OutreachAgent(FakeOutreachService()),
        reviewer_agent=ReviewerAgent(FakeReviewerService()),
    )

    result = LeadPilotState.model_validate(
        failing_workflow.invoke(
            LeadPilotState(company=CompanyState(website="https://example.com"))
        )
    )

    assert result.execution.status is WorkflowStatus.FAILED
    assert result.execution.current_agent == "ResearchAgent"
    assert result.execution.errors == ["Firecrawl unavailable"]
    assert downstream_calls == []
