from sqlalchemy.orm import Session

from app.models.workflow_run import WorkflowRun
from app.schemas.state import LeadPilotState


class WorkflowRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, state: LeadPilotState):

        run = WorkflowRun(
            company_name=state.company.company_name,
            website=state.company.website,
            status=state.execution.status.value,
            qualification_score=state.qualification.score or 0,
            workflow_data=state.model_dump(mode="json"),
        )

        self.db.add(run)
        self.db.commit()
        self.db.refresh(run)

        return run