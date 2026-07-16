from datetime import datetime, UTC

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.workflow_run import WorkflowRun
from app.schemas.state import LeadPilotState
from app.schemas.workflow import WorkflowRequest
from app.services.workflow_service import WorkflowService
from app.workflows.lead_pipeline import lead_pipeline

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.post("/run")
def run_workflow(
    request: WorkflowRequest,
    db: Session = Depends(get_db),
):
    workflow_start = datetime.now(UTC)

    state = LeadPilotState()
    state.company.company_name = request.company_name
    state.company.website = str(request.website)

    result = LeadPilotState.model_validate(
        lead_pipeline.invoke(state)
    )

    workflow_end = datetime.now(UTC)

    result.metadata.started_at = workflow_start
    result.metadata.completed_at = workflow_end
    result.metadata.execution_time = round(
        (workflow_end - workflow_start).total_seconds(),
        2,
    )

    run = WorkflowService(db).save_run(result)

    # Keep metadata in sync with the persisted workflow
    result.metadata.workflow_id = run.id

    return {
        "workflow_id": run.id,
        "status": result.execution.status.value,
        "qualification_score": result.qualification.score,
        "data": result.model_dump(),
    }


@router.get("/history")
def history(db: Session = Depends(get_db)):
    return (
        db.query(WorkflowRun)
        .order_by(WorkflowRun.created_at.desc())
        .all()
    )


@router.get("/{workflow_id}")
def get_workflow(
    workflow_id: int,
    db: Session = Depends(get_db),
):
    return (
        db.query(WorkflowRun)
        .filter(WorkflowRun.id == workflow_id)
        .first()
    )