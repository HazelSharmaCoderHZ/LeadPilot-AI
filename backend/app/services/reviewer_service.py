from app.schemas.state import LeadPilotState
from app.services.providers.llm.base import BaseLLM


class ReviewerService:

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def review_email(self, state: LeadPilotState):

        result = self.llm.review_email(
            subject=state.outreach.subject or "",
            body=state.outreach.body or "",
        )

        return result
