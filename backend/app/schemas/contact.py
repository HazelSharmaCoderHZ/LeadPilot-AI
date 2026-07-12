from pydantic import BaseModel


class ContactResult(BaseModel):
    name: str
    title: str
    email: str | None = None
    linkedin: str | None = None
    confidence: float = 0.0