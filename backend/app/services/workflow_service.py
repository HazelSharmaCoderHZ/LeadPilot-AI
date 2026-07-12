from sqlalchemy.orm import Session

from app.repositories.workflow_repository import WorkflowRepository
from app.schemas.state import LeadPilotState


class WorkflowService:

    def __init__(self, db: Session):
        self.repo = WorkflowRepository(db)

    def save_run(self, state: LeadPilotState):
        return self.repo.create(state)