
from app.schemas.research import ResearchResult
from app.services.providers.crawlers.base import BaseCrawler

class ResearchService:
    def __init__(self, crawler: BaseCrawler):
        self.crawler = crawler

    def research(self, website: str) -> ResearchResult:
        result = self.crawler.scrape(website)

        if not result.success:
            raise Exception(result.error)

        metadata = result.metadata or {}

        return ResearchResult(
            website=website,
            company_name=metadata.get("og_site_name")
            or metadata.get("og_site_name")
            or metadata.get("siteName")
            or metadata.get("title"),
            title=result.title,
            description=metadata.get("description"),
            language=metadata.get("language"),
            raw_markdown=result.markdown,
            metadata=metadata,
        )
