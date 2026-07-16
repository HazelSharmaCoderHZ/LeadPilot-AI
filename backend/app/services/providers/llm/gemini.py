import json
from typing import Type, TypeVar

from google import genai
from google.genai import types
from pydantic import BaseModel

from app.core.config import settings
from app.schemas.analysis import AnalysisResult
from app.schemas.outreach import OutreachResult
from app.schemas.qualification import QualificationResult
from app.schemas.review import ReviewResult
from app.services.providers.llm.base import BaseLLM

T = TypeVar("T", bound=BaseModel)


class GeminiProvider(BaseLLM):

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.GEMINI_MODEL

    def _generate_json(self, prompt: str) -> dict:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature=0.2,
            ),
        )

        return json.loads(response.text)

    def generate_structured(
        self,
        prompt: str,
        schema: Type[T],
    ) -> T:
        """
        Generate structured JSON using Gemini and validate it against the
        supplied Pydantic schema.
        """
        return schema(**self._generate_json(prompt))

    def analyze(self, markdown: str) -> AnalysisResult:

        prompt = f"""
Analyze the following company website.

Return ONLY valid JSON.

{{
  "company_name":"",
  "industry":"",
  "company_description":"",
  "business_model":"",
  "offerings":[],
  "target_customers":[],
  "pain_points":[],
  "tech_stack":[]
}}

Website:

{markdown}
"""

        return self.generate_structured(prompt, AnalysisResult)

    def qualify(
        self,
        company_name: str,
        industry: str,
        summary: str,
        contacts_found: int,
    ) -> QualificationResult:

        prompt = f"""
You are an outbound sales expert.

Score this company from 0-100.

Company Name:
{company_name}

Industry:
{industry}

Summary:
{summary}

Contacts Found:
{contacts_found}

Return ONLY valid JSON.

{{
    "score":95,
    "tier":"A",
    "reasoning":""
}}
"""

        return self.generate_structured(prompt, QualificationResult)

    def generate_outreach_email(
        self,
        company_name: str,
        industry: str,
        summary: str,
        pain_points: list[str],
        contact_name: str,
        contact_role: str,
    ) -> OutreachResult:

        prompt = f"""
You are an expert B2B SDR.

Generate a personalized cold email.

Company:
{company_name}

Industry:
{industry}

Summary:
{summary}

Pain Points:
{", ".join(pain_points)}

Decision Maker:
{contact_name}

Role:
{contact_role}

Return ONLY valid JSON.

{{
    "subject":"",
    "body":"",
    "cta":"",
    "personalization_summary":""
}}
"""

        return self.generate_structured(prompt, OutreachResult)

    def review_email(
        self,
        subject: str,
        body: str,
    ) -> ReviewResult:

        prompt = f"""
You are an expert sales email reviewer.

Review the following email.

Check:
- Personalization
- Grammar
- Clarity
- Tone
- CTA
- Spam risk

Return ONLY valid JSON.

{{
    "approved": true,
    "score": 95,
    "feedback": [],
    "revised_subject": "",
    "revised_body": ""
}}

Subject:
{subject}

Body:
{body}
"""

        return self.generate_structured(prompt, ReviewResult)