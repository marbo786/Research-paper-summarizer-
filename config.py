import os

API_PROVIDER = os.getenv("API_PROVIDER", "openai").strip().lower()
API_KEY = os.getenv("API_KEY") or os.getenv(
    "HF_TOKEN" if API_PROVIDER == "huggingface" else "OPENAI_API_KEY", ""
)
MODEL_NAME = os.getenv("MODEL_NAME", "")
