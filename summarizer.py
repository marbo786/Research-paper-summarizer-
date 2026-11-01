from config import API_PROVIDER, API_KEY, MODEL_NAME

def summarize_text(text_chunk):
    if not text_chunk.strip():
        return ""
    if not API_KEY or not MODEL_NAME:
        raise ValueError("Configure an API key and MODEL_NAME before summarizing.")
    if API_PROVIDER == "openai":
        from openai_client import summarize_with_openai
        return summarize_with_openai(API_KEY, MODEL_NAME, text_chunk)
    
    elif API_PROVIDER == "huggingface":
        from hf_client import summarize_with_huggingface
        return summarize_with_huggingface(API_KEY, MODEL_NAME, text_chunk)
    
    else:
        raise ValueError("Unsupported API provider selected.")
