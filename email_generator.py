from huggingface_hub import InferenceClient
import config

client = InferenceClient(api_key=config.HF_TOKEN)

def generate_email(company, solution):
    prompt = f"""
    Write a highly personalized B2B cold email from {config.FOCUS_SOFTNET_NAME}.
    Company: {company['name']}
    Address: {company.get('address')}
    Solution: {solution}
    Requirements: Professional, Request demo meeting, Under 140 words.
    """

    res = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250
    )

    return res.choices[0].message.content