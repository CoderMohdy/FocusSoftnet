from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

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