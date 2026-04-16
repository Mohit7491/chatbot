import requests

# 👉 user input
user_input = input("Ask something: ")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": user_input}
    ]
}

response = requests.post(url, headers=headers, json=data)

result = response.json()

answer = result["choices"][0]["message"]["content"]

# 👇 file save system
with open("conversation.txt", "a") as f:
    f.write("User: " + user_input + "\n")
    f.write("AI: " + answer + "\n\n")
print("\nAI:", answer)