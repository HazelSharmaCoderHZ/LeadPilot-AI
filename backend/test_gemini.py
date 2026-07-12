from types import SimpleNamespace

from app.services.providers.llm.gemini import GeminiProvider


def test_generate_json_uses_provider_client_without_network(monkeypatch):
    provider = GeminiProvider()
    calls = []

    def generate_content(**kwargs):
        calls.append(kwargs)
        return SimpleNamespace(text='{"company_name": "Example Co"}')

    monkeypatch.setattr(
        provider.client.models,
        "generate_content",
        generate_content,
    )

    assert provider._generate_json("Summarize this") == {
        "company_name": "Example Co"
    }
    assert calls[0]["model"] == provider.model
    assert calls[0]["contents"] == "Summarize this"
