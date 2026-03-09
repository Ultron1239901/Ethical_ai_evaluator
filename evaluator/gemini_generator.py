import os
import requests
import time

API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

MODEL = "meta-llama/llama-3.1-8b-instruct"

def generate_response(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    if not API_KEY:
        return "API key not configured. Set OPENROUTER_API_KEY in environment."

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "Ethical AI Evaluator"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    messages = [
    {"role": "system", "content": "You are a responsible AI. Refuse harmful or illegal requests."},
    {"role": "user", "content": prompt}
    ]

    response = requests.post(url, headers=headers, json={"model": MODEL, "messages": messages})

    result = response.json()

    # safety fallback
    if "choices" not in result:
        return "Model temporarily unavailable. Please try again."

    time.sleep(1)  # prevents hitting rate limits

    return result["choices"][0]["message"]["content"]
