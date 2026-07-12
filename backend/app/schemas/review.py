from pydantic import BaseModel, Field


class ReviewResult(BaseModel):
    approved: bool
    score: int
    feedback: list[str] = Field(default_factory=list)
    revised_subject: str
    revised_body: str