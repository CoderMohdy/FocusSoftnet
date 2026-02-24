from huggingface_hub import InferenceClient
import config

client = InferenceClient(api_key=config.HF_TOKEN)

def qualifies(company_name, solution):
    prompt = f"Company: {company_name}\nSolution: {solution}\n\nDoes this company likely need this software? Answer YES or NO with one line reason."

    res = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    return res.choices[0].message.content