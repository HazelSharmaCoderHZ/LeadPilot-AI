from abc import ABC, abstractmethod

from app.schemas.search import SearchResult


class BaseSearchProvider(ABC):

    @abstractmethod
    def search(
        self,
        company_name: str,
        website: str,
    ) -> list[SearchResult]:
        """
        Search for publicly available information about a company.

        The provider should NOT attempt to extract contacts.
        It should only return relevant search results.

        Contact extraction is handled by the LLM layer.
        """
        ...