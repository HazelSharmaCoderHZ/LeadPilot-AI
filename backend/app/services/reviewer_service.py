from app.schemas.state import LeadPilotState
from app.services.providers.llm.gemini import GeminiProvider


class ReviewerService:

    def __init__(self):
        self.llm = GeminiProvider()

    def review_email(self, state: LeadPilotState):

        result = self.llm.review_email(
            subject=state.outreach.subject or "",
            body=state.outreach.body or "",
        )

        return result