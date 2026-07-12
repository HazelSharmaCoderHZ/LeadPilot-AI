from pydantic import BaseModel, HttpUrl


class WorkflowRequest(BaseModel):
    company_name: str
    website: HttpUrl


class WorkflowResponse(BaseModel):
    workflow_id: int
    status: str
    qualification_score: int | None
    data: dict