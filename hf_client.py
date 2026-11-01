def summarize_with_huggingface(api_key, model_name, text):
    from huggingface_hub import InferenceClient

    with InferenceClient(provider="hf-inference", api_key=api_key, timeout=60) as client:
        result = client.summarization(text, model=model_name)
    if not result.summary_text:
        raise ValueError("The provider returned no summary.")
    return result.summary_text.strip()
