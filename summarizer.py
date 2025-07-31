from openai import OpenAI

client = OpenAI(api_key="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")

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an academic summarization assistant. "
                    "Generate a long, structured summary of the paper including its purpose, methods, results, and conclusions. "
                    "The summary should be detailed and at least 600-800 words if the paper is long."
                )
            },
            {
                "role": "user",
                "content": f"Summarize the following research paper:\n\n{text}"
            }
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content
