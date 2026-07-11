from pydantic import BaseModel, Field


class AnalysisResult(BaseModel):
    company_name: str | None = None

    industry: str | None = None
    company_description: str | None = None
    business_model: str | None = None

    offerings: list[str] = Field(default_factory=list)
    target_customers: list[str] = Field(default_factory=list)
    pain_points: list[str] = Field(default_factory=list)
    tech_stack: list[str] = Field(default_factory=list)