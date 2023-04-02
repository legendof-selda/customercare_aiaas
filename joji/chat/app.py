import openai
import joji
import streamlit as st

from streamlit_chat import message

joji.initialize_openai()


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message


# Creating the chatbot interface
st.title("Customer Care")

# Storing the chat
if "chat" not in st.session_state:
    st.session_state["chat"] = []


def user_chat(message: str):
    st.session_state.chat.append({"message": message, "is_user": True, "key": generate_message_id()})


def ai_chat(message: str):
    st.session_state.chat.append({"message": message, "is_user": False, "key": generate_message_id()})


def display_message(chat_message: dict):
    message(chat_message["message"], is_user=chat_message["is_user"], key=chat_message["key"])


def display_chat_history():
    for i, chat_message in enumerate(st.session_state["chat"]):
        display_message(chat_message)


def generate_message_id():
    return len(st.session_state["chat"])


def history_available() -> bool:
    return bool(len(st.session_state["chat"]))


# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ", placeholder="Hello, how are you?", key="input", help="Enter prompt here!")
    return input_text


if history_available():
    display_chat_history()

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output
    user_chat(user_input)
    ai_chat(output)
