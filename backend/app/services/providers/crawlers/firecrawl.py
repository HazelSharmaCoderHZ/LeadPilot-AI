from firecrawl import FirecrawlApp

from app.core.config import settings
from app.schemas.crawler import CrawlerResult
from app.services.providers.crawlers.base import BaseCrawler


class FirecrawlCrawler(BaseCrawler):
    def __init__(self):
        self.client = FirecrawlApp(api_key=settings.FIRECRAWL_API_KEY)

    def scrape(self, url: str) -> CrawlerResult:
        try:
            response = self.client.scrape(
                url,
                formats=["markdown", "html"],
            )

            metadata = response.metadata_dict

            return CrawlerResult(
                success=True,
                url=url,
                title=metadata.get("title"),
                markdown=response.markdown,
                html=response.html,
                metadata=metadata,
                links=response.links or [],
                status_code=metadata.get("status_code", 200),
            )

        except Exception as e:
            return CrawlerResult(
                success=False,
                url=url,
                error=str(e),
            )
