from app.schemas.state import (
    LeadPilotState,
    CompanyState,
)
state = LeadPilotState(
    company=CompanyState(
        company_name="OpenAI",
        website="https://openai.com",
    )
)

print(state.model_dump_json(indent=2))