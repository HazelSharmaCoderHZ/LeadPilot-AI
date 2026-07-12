from abc import ABC, abstractmethod

from app.schemas.contact import ContactResult


class BaseSearchProvider(ABC):

    @abstractmethod
    def find_contacts(
        self,
        company_name: str,
        website: str,
    ) -> list[ContactResult]:
        ...