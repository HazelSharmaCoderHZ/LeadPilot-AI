from pydantic import AliasChoices, BaseModel, Field


class ContactResult(BaseModel):
    name: str
    role: str = Field(validation_alias=AliasChoices("role", "title"))
    email: str | None = None
    linkedin: str | None = None
    confidence: float = 0.0


class ContactExtractionResult(BaseModel):
    """
    Structured response returned by the LLM when extracting
    decision makers from Tavily search results.
    """

    contacts: list[ContactResult]