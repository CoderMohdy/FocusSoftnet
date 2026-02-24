from openai import OpenAI
import config

# FIX: Changed 'OPENAI_API_KEY =' to 'api_key='
# IMPORTANT: Delete the hardcoded "sk-proj..." key from your file immediately!
client = OpenAI(api_key=config.OPENAI_API_KEY)

def qualifies(company_name, solution):
    prompt = f"""
    Company: {company_name}
    Solution: {solution}

    Does this company likely need this software?
    Answer YES or NO with one line reason.
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content