from config import API_PROVIDER, API_KEY, MODEL_NAME

def summarize_text(text_chunk):
    if API_PROVIDER == "openai":
        from openai_client import summarize_with_openai
        return summarize_with_openai(API_KEY, MODEL_NAME, text_chunk)
    
    elif API_PROVIDER == "huggingface":
        from hf_client import summarize_with_huggingface
        return summarize_with_huggingface(API_KEY, MODEL_NAME, text_chunk)
    
    else:
        raise ValueError("Unsupported API provider selected.")
