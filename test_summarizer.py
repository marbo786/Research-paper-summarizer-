from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
import summarizer
from openai_client import summarize_with_openai
from hf_client import summarize_with_huggingface


def test_missing_configuration(monkeypatch):
    monkeypatch.setattr(summarizer, "API_KEY", "")
    with pytest.raises(ValueError, match="Configure"):
        summarizer.summarize_text("A paper")


def test_empty_text():
    assert summarizer.summarize_text("  ") == ""


def test_openai_request_and_response():
    sdk = MagicMock()
    client = sdk.OpenAI.return_value.__enter__.return_value
    client.chat.completions.create.return_value = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=" Summary "))]
    )
    with patch.dict("sys.modules", {"openai": sdk}):
        assert summarize_with_openai("test-key", "test-model", "Paper") == "Summary"
    assert client.chat.completions.create.call_args.kwargs["model"] == "test-model"
    assert client.chat.completions.create.call_args.kwargs["messages"][-1]["content"] == "Paper"


def test_huggingface_request_and_response():
    sdk = MagicMock()
    client = sdk.InferenceClient.return_value.__enter__.return_value
    client.summarization.return_value = SimpleNamespace(summary_text=" Summary ")
    with patch.dict("sys.modules", {"huggingface_hub": sdk}):
        assert summarize_with_huggingface("test-key", "test-model", "Paper") == "Summary"
    client.summarization.assert_called_once_with("Paper", model="test-model")


@pytest.mark.parametrize("provider, module, function", [
    ("openai", "openai_client", "summarize_with_openai"),
    ("huggingface", "hf_client", "summarize_with_huggingface"),
])
def test_dispatch(monkeypatch, provider, module, function):
    monkeypatch.setattr(summarizer, "API_PROVIDER", provider)
    monkeypatch.setattr(summarizer, "API_KEY", "test-key")
    monkeypatch.setattr(summarizer, "MODEL_NAME", "test-model")
    with patch(f"{module}.{function}", return_value="Summary") as call:
        assert summarizer.summarize_text("Paper") == "Summary"
    call.assert_called_once_with("test-key", "test-model", "Paper")
