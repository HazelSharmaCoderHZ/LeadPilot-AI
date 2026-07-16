from tavily import TavilyClient

from app.core.config import settings
from app.schemas.search import SearchResult
from app.services.providers.search.base import BaseSearchProvider


class TavilyProvider(BaseSearchProvider):

    def __init__(self):
        self.client = TavilyClient(api_key=settings.TAVILY_API_KEY)

    def search(
        self,
        company_name: str,
        website: str,
    ) -> list[SearchResult]:

        queries = [
            f"{company_name} CEO",
            f"{company_name} Founder",
            f"{company_name} Leadership Team",
            f"{company_name} Executive Team",
            f"site:linkedin.com {company_name}",
        ]

        if website:
            queries.append(f"site:{website} leadership")

        seen_urls: set[str] = set()
        results: list[SearchResult] = []

        for query in queries:

            response = self.client.search(
                query=query,
                search_depth="advanced",
                max_results=3,
            )

            for item in response.get("results", []):

                url = item.get("url")

                if not url or url in seen_urls:
                    continue

                seen_urls.add(url)

                results.append(
                    SearchResult(
                        title=item.get("title", ""),
                        url=url,
                        content=item.get("content", ""),
                        raw_content=item.get("raw_content"),
                    )
                )

        return results