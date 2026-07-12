from datetime import datetime
from typing import Any
from enum import Enum
from pydantic import BaseModel, Field
class CompanyState(BaseModel):
    company_name: str | None = None
    website: str | None = None
    linkedin: str | None = None
    industry: str | None = None
    location: str | None = None


class WorkflowStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class ResearchState(BaseModel):
    company_name: str | None = None
    title: str | None = None
    description: str | None = None
    summary: str | None = None
    language: str | None = None
    mission: str | None = None
    products: list[str] = Field(default_factory=list)
    target_audience: str | None = None
    company_size: str | None = None
    recent_news: list[str] = Field(default_factory=list)


class ScrapedContentState(BaseModel):
    website: str | None = None
    markdown: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
    homepage: str | None = None
    about: str | None = None
    pricing: str | None = None
    careers: str | None = None
    blog: str | None = None
    tech_stack: list[str] = Field(default_factory=list)


class AnalysisState(BaseModel):
    summary: str | None = None
    business_model: str | None = None
    pain_points: list[str] = Field(default_factory=list)
    opportunities: list[str] = Field(default_factory=list)
    competitors: list[str] = Field(default_factory=list)

class ContactState(BaseModel):
    name: str | None = None
    role: str | None = None
    email: str | None = None
    linkedin: str | None = None

class QualificationState(BaseModel):
    score: int | None = None
    tier: str | None = None
    reasoning: str | None = None


class OutreachState(BaseModel):
    subject: str | None = None
    body: str | None = None
    cta: str | None = None
    personalization_summary: str | None = None


class ReviewState(BaseModel):
    approved: bool = False
    score: int | None = None
    feedback: list[str] = Field(default_factory=list)
    revised_subject: str | None = None
    revised_body: str | None = None


class ExecutionState(BaseModel):
    current_agent: str | None = None
    status: WorkflowStatus = WorkflowStatus.PENDING
    errors: list[str] = Field(default_factory=list)

class MetadataState(BaseModel):
    workflow_id: str | None = None
    workflow_version: str = "v1"
    execution_time: float = 0.0
    llm_provider: str = "gemini"
    llm_model: str = "gemini-3.1-flash-lite"

    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: datetime | None = None

    token_usage: int = 0
    estimated_cost: float = 0.0


class LeadPilotState(BaseModel):
    company: CompanyState = Field(default_factory=CompanyState)
    agent_outputs: dict[str, Any] = Field(default_factory=dict)
    research: ResearchState = Field(default_factory=ResearchState)
    scraped_content: ScrapedContentState = Field(default_factory=ScrapedContentState)
    analysis: AnalysisState = Field(default_factory=AnalysisState)
    contacts: list[ContactState] = Field(default_factory=list)
    qualification: QualificationState = Field(default_factory=QualificationState)
    outreach: OutreachState = Field(default_factory=OutreachState)
    review: ReviewState = Field(default_factory=ReviewState)
    execution: ExecutionState = Field(default_factory=ExecutionState)
    metadata: MetadataState = Field(default_factory=MetadataState)
    context: dict[str, Any] = Field(default_factory=dict)
