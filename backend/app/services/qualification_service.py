from app.schemas.qualification import QualificationResult
from app.services.providers.llm.base import BaseLLM


class QualificationService:

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def qualify(
        self,
        company_name: str,
        industry: str,
        summary: str,
        contacts_found: int,
    ) -> QualificationResult:

        return self.llm.qualify(
            company_name=company_name,
            industry=industry,
            summary=summary,
            contacts_found=contacts_found,
        )
