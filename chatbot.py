from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
import requests
url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


messages = [
    {"role": "system", "content": "You are a strict AI mentor. Give clear, step-by-step answers."}
]
# 👉 user input
while True:
    user_input = input("Ask something: ")
    if user_input.lower() == "exit":
      break
    messages.append({"role": "user", "content": user_input})

    data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": messages
    }
    

    response = requests.post(url, headers=headers, json=data)

    result = response.json()
    
     # 🔐 safety check (important)
    if "choices" not in result:
        print("Error:", result)
        continue
    answer = result["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": answer})
    
    print("\nAI:", answer)
    # 👇 file save system
    with open("conversation.txt", "a") as f:
      f.write("User: " + user_input + "\n")
      f.write("AI: " + answer + "\n\n")
