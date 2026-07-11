from firecrawl import FirecrawlApp

from app.core.config import settings
from app.schemas.crawler import CrawlerResult
from app.services.providers.crawler.base import BaseCrawler


class FirecrawlCrawler(BaseCrawler):
    def __init__(self):
        self.client = FirecrawlApp(api_key=settings.firecrawl_api_key)

    def scrape(self, url: str) -> CrawlerResult:
        try:
            response = self.client.scrape_url(
                url=url,
                formats=["markdown", "html"],
            )

            metadata = response.get("metadata", {})

            return CrawlerResult(
                success=True,
                url=url,
                title=metadata.get("title"),
                markdown=response.get("markdown"),
                html=response.get("html"),
                metadata=metadata,
                links=response.get("links", []),
                status_code=200,
            )

        except Exception as e:
            return CrawlerResult(
                success=False,
                url=url,
                error=str(e),
            )