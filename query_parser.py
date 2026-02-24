from huggingface_hub import InferenceClient
import config
import json

client = InferenceClient(api_key=config.HF_TOKEN)

def parse_query(user_query):
    prompt = f"Extract the software solution and search keywords from: {user_query}. Return ONLY a JSON object with keys 'solution' and 'keywords' (list)."

    res = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )

    return res.choices[0].message.content