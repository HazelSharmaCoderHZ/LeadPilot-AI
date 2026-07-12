from app.services.providers.llm.gemini import GeminiProvider


class AnalysisService:

    def __init__(self):
        self.llm = GeminiProvider()

    def analyze(self, markdown: str):
        return self.llm.analyze(markdown)