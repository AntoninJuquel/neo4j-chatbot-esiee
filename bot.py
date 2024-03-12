import streamlit as st
from utils import write_message
from agent import generate_response

st.set_page_config("CineBot", page_icon=":movie_camera:")

if "messages" not in st.session_state:
    bot_prompt = """
Welcome to the Movie Assistant Chatbot!  
I'm here to assist you with all things movies. Feel free to ask any movie-related questions, and I'll provide you with the information you're looking for. Whether it's details about actors, popular movies, or recommendations based on your preferences – I've got you covered. Let's dive into the world of cinema together! 🎬🤖
"""
    st.session_state.messages = [
        {"role": "assistant", "content": bot_prompt},
    ]


def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    with st.spinner('Thinking...'):
        response = generate_response(message)
        write_message('assistant', response)


for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

if prompt := st.chat_input("Message CineBot..."):
    write_message('user', prompt)
    handle_submit(prompt)
