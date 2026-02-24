from openai import OpenAI
import config

client = OpenAI(OPENAI_API_KEY = "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")

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