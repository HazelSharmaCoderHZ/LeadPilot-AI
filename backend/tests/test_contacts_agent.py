from app.agents.contacts_agent import ContactsAgent
from app.schemas.contact import ContactResult
from app.schemas.state import CompanyState, ContactState, LeadPilotState


class FakeContactsService:
    def find_contacts(self, company_name: str, website: str) -> list[ContactResult]:
        return [
            ContactResult(
                name="Ada Lovelace",
                role="Chief Executive Officer",
                email="ada@example.com",
            )
        ]


def test_contacts_agent_converts_results_to_workflow_contact_contract():
    agent = ContactsAgent(FakeContactsService())

    result = agent.execute(
        LeadPilotState(
            company=CompanyState(
                company_name="Example Co",
                website="https://example.com",
            )
        )
    )

    assert result.contacts == [
        ContactState(
            name="Ada Lovelace",
            role="Chief Executive Officer",
            email="ada@example.com",
        )
    ]
    assert result.model_dump(mode="json")["contacts"][0] == {
        "name": "Ada Lovelace",
        "role": "Chief Executive Officer",
        "email": "ada@example.com",
        "linkedin": None,
    }


def test_contact_result_accepts_legacy_title_but_serializes_role():
    contact = ContactResult(name="Ada Lovelace", title="CEO")

    assert contact.role == "CEO"
    assert contact.model_dump() == {
        "name": "Ada Lovelace",
        "role": "CEO",
        "email": None,
        "linkedin": None,
        "confidence": 0.0,
    }
