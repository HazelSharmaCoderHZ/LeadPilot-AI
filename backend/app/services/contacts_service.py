from app.schemas.contact import ContactExtractionResult, ContactResult
from app.services.providers.llm.base import BaseLLM
from app.services.providers.search.base import BaseSearchProvider


class ContactsService:

    def __init__(
        self,
        provider: BaseSearchProvider,
        llm: BaseLLM,
    ):
        self.provider = provider
        self.llm = llm

    def find_contacts(
        self,
        company_name: str,
        website: str,
    ) -> list[ContactResult]:

        search_results = self.provider.search(
            company_name,
            website,
        )

        if not search_results:
            return []

        context = "\n\n".join(
            f"""
Title:
{result.title}

URL:
{result.url}

Snippet:
{result.content}

Raw Content:
{result.raw_content or "N/A"}
"""
            for result in search_results
        )

        prompt = f"""
You are an expert B2B sales researcher.

Identify the most relevant decision makers for the following company.

Prefer:
- CEO
- Founder
- Co-Founder
- CTO
- COO
- VP Engineering
- Head of Engineering
- Director
- Decision makers

Return ONLY valid JSON.

{{
  "contacts": [
    {{
      "name": "",
      "role": "",
      "email": null,
      "linkedin": null,
      "confidence": 0.0
    }}
  ]
}}

Company:
{company_name}

Website:
{website}

Search Results:

{context}
"""

        extraction = self.llm.generate_structured(
            prompt,
            ContactExtractionResult,
        )

        return extraction.contacts