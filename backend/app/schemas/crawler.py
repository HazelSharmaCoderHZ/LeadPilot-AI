from pydantic import BaseModel, Field


class CrawlerResult(BaseModel):
    success: bool
    url: str

    title: str | None = None
    markdown: str | None = None
    html: str | None = None

    metadata: dict = Field(default_factory=dict)
    links: list[str] = Field(default_factory=list)

    status_code: int | None = None
    error: str | None = None