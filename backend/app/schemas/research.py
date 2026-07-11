from pydantic import BaseModel, Field


class ResearchResult(BaseModel):
    website: str

    company_name: str | None = None
    title: str | None = None
    description: str | None = None
    summary: str | None = None
    language: str | None = None

    raw_markdown: str | None = None

    metadata: dict = Field(default_factory=dict)