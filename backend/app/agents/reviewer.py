from app.agents.base import BaseAgent
from app.schemas.state import LeadPilotState
from app.services.reviewer_service import ReviewerService


class ReviewerAgent(BaseAgent):

    def __init__(self, service: ReviewerService):
        super().__init__()
        self.service = service

    def run(self, state: LeadPilotState):

        result = self.service.review_email(state)

        state.review.approved = result.approved
        state.review.score = result.score
        state.review.feedback = result.feedback
        state.review.revised_subject = result.revised_subject
        state.review.revised_body = result.revised_body

        return state
