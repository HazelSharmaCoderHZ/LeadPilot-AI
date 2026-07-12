from app.schemas.state import (
    LeadPilotState,
    CompanyState,
)

def test_state_serializes_company_data():
    state = LeadPilotState(
        company=CompanyState(
            company_name="OpenAI",
            website="https://openai.com",
        )
    )

    payload = state.model_dump(mode="json")

    assert payload["company"] == {
        "company_name": "OpenAI",
        "website": "https://openai.com",
        "linkedin": None,
        "industry": None,
        "location": None,
    }
