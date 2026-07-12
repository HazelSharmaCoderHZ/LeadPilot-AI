from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.workflow_run import WorkflowRun
from app.db.session import get_db
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

    state = LeadPilotState()

    state.company.company_name = request.company_name
    state.company.website = str(request.website)

    result = LeadPilotState.model_validate(
        lead_pipeline.invoke(state)
    )

    run = WorkflowService(db).save_run(result)

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