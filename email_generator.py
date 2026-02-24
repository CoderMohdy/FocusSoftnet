from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def generate_email(company, solution):
    prompt = f"""
    Write a highly personalized B2B cold email from {config.FOCUS_SOFTNET_NAME}.

    Company: {company['name']}
    Address: {company.get('address')}
    Solution: {solution}

    Requirements:
    - Professional
    - Request demo meeting
    - Not generic
    - Under 140 words
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content