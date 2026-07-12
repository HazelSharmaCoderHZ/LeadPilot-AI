from pydantic import BaseModel


class QualificationResult(BaseModel):
    score: int
    tier: str
    reasoning: str