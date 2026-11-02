import streamlit as st
from huggingface_hub import InferenceClient


st.title("Chatbot by bngoc")


# Sidebar nhập token
with st.sidebar:
    st.title("Hugging Face account")

    hf_token = st.text_input(
        "Hugging Face token",
        type="password"
    )


# Khởi tạo lịch sử chat một lần
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "How may I help you?"
        }
    ]


# Hiển thị lịch sử tin nhắn
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def generate_response(messages, token):
    client = InferenceClient(
        provider="auto",
        api_key=token
    )

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=messages,
        max_tokens=500
    )

    return response.choices[0].message.content


prompt = st.chat_input(
    "Type your message",
    disabled=not hf_token
)


if prompt:
    # Lưu tin nhắn người dùng
    user_message = {
        "role": "user",
        "content": prompt
    }

    st.session_state.messages.append(user_message)

    # Hiển thị tin nhắn người dùng
    with st.chat_message("user"):
        st.write(prompt)

    # Sinh câu trả lời
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = generate_response(
                    st.session_state.messages,
                    hf_token
                )

                st.write(response)

            except Exception as error:
                response = f"API error: {error}"
                st.error(response)

    # Lưu câu trả lời assistant
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )