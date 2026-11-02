from huggingface_hub import InferenceClient


hf_token = input("Enter your Hugging Face token: ")

client = InferenceClient(
    provider="auto",
    api_key=hf_token
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "Hello, introduce yourself briefly."
        }
    ],
    max_tokens=200
)

print(response.choices[0].message.content)