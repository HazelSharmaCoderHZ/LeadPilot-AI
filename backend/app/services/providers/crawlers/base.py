from abc import ABC, abstractmethod

from app.schemas.crawler import CrawlerResult


class BaseCrawler(ABC):

    @abstractmethod
    def scrape(self, url: str) -> CrawlerResult:
        ...