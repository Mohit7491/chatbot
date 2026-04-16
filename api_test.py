import requests

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "text/plain"
}
data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "What is trading?"}
    ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

# 👉 यही main line है
answer = result["choices"][0]["message"]["content"]

print(answer)