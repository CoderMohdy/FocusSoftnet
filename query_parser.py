from openai import OpenAI
import config

client = OpenAI(OPENAI_API_KEY = "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")

def parse_query(user_query):
    prompt = f"""
    Extract the software solution and search keywords.

    Query: {user_query}

    Return JSON with:
    - solution
    - keywords (list)
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content