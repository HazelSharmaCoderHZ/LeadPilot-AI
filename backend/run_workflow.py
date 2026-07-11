from app.schemas.state import LeadPilotState
from app.workflows.lead_pipeline import lead_pipeline

def main():

    state = LeadPilotState()

    result = lead_pipeline.invoke(state)

    result = LeadPilotState.model_validate(result)
    print("\nWorkflow completed!\n")

    print("Type:", type(result))
    print(type(result))


if __name__ == "__main__":
    main()