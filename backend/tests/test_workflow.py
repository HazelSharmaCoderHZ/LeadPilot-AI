from app.schemas.state import LeadPilotState
from app.workflows.lead_pipeline import lead_pipeline


def test_dummy_workflow():

    state = LeadPilotState(
        company=CompanyState(
            website="https://openai.com"
        )
    )

    result = await graph.ainvoke(state.model_dump())