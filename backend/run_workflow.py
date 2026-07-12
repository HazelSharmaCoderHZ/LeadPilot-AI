from app.schemas.state import LeadPilotState, CompanyState
from app.workflows.lead_pipeline import lead_pipeline


def main():

    state = LeadPilotState(
        company=CompanyState(
            website="https://openai.com"
        )
    )

    result = lead_pipeline.invoke(state)

    result = LeadPilotState.model_validate(result)

    print("\nWorkflow completed!\n")
    print(result)
    print(state.review.model_dump())


if __name__ == "__main__":
    main()