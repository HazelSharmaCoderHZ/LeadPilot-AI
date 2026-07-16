from abc import ABC, abstractmethod
from typing import Type, TypeVar

from pydantic import BaseModel

from app.schemas.analysis import AnalysisResult
from app.schemas.outreach import OutreachResult
from app.schemas.qualification import QualificationResult
from app.schemas.review import ReviewResult

T = TypeVar("T", bound=BaseModel)


class BaseLLM(ABC):
    """
    Base interface for all LLM providers.

    Providers should expose a generic structured-generation method while
    optionally providing higher-level convenience methods for common tasks.
    """

    @abstractmethod
    def generate_structured(
        self,
        prompt: str,
        schema: Type[T],
    ) -> T:
        """
        Generate structured JSON output and validate it against the supplied
        Pydantic schema.
        """
        ...

    @abstractmethod
    def analyze(self, markdown: str) -> AnalysisResult:
        ...

    @abstractmethod
    def qualify(
        self,
        company_name: str,
        industry: str,
        summary: str,
        contacts_found: int,
    ) -> QualificationResult:
        ...

    @abstractmethod
    def generate_outreach_email(
        self,
        company_name: str,
        industry: str,
        summary: str,
        pain_points: list[str],
        contact_name: str,
        contact_role: str,
    ) -> OutreachResult:
        ...

    @abstractmethod
    def review_email(
        self,
        subject: str,
        body: str,
    ) -> ReviewResult:
        ...