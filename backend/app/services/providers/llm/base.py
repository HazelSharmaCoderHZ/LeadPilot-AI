from abc import ABC, abstractmethod

from app.schemas.analysis import AnalysisResult


class BaseLLM(ABC):

    @abstractmethod
    def analyze(self, markdown: str) -> AnalysisResult:
        ...