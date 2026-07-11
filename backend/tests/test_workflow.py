from app.schemas.state import LeadPilotState
from app.workflows.lead_pipeline import lead_pipeline


def test_dummy_workflow():

    state = LeadPilotState()

    result = lead_pipeline.invoke(state)

    assert isinstance(result, LeadPilotState)