from app.services.providers.llm.base import BaseLLM


class AnalysisService:

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def analyze(self, markdown: str):
        return self.llm.analyze(markdown)
