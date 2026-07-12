from app.services.providers.search.tavily import TavilyProvider


class ContactsService:

    def __init__(self):
        self.provider = TavilyProvider()

    def find_contacts(
        self,
        company_name: str,
        website: str,
    ):
        return self.provider.find_contacts(
            company_name,
            website,
        )