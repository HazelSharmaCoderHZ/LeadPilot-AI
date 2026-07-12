from pydantic import BaseModel


class OutreachResult(BaseModel):
    subject: str
    body: str
    cta: str
    personalization_summary: str