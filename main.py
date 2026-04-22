import requests
import sys

# Using Groq's free API - get your key at https://console.groq.com
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"
API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def query_llm(question: str) -> str:
    try:
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": question}],
            "max_tokens": 512
        }
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)

        if response.status_code != 200:
            return f"API Error {response.status_code}: {response.text}"

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"


def main():
    print("=== AI Question Answering System ===")

    try:
        user_input = input("Enter your question: ").strip()

        if not user_input:
            print("Error: Question cannot be empty.")
            sys.exit(1)

        print("Thinking...")
        response = query_llm(user_input)

        print("\n--- AI Response ---")
        print(response)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
