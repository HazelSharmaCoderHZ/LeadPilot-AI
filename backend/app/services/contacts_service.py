from app.schemas.contact import ContactResult
from app.services.providers.search.base import BaseSearchProvider


class ContactsService:

    def __init__(self, provider: BaseSearchProvider):
        self.provider = provider

    def find_contacts(
        self,
        company_name: str,
        website: str,
    ) -> list[ContactResult]:
        return self.provider.find_contacts(
            company_name,
            website,
        )
