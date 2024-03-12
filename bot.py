import streamlit as st
from agent import generate_response
from utils import write_message

# tag::setup[]
# Page Config
st.set_page_config("CineBot", page_icon=":movie_camera:")

key_choice = st.sidebar.radio(
    "OpenAI API Key",
    (
        "Your Key",
        "Free Key (capped)",
    ),
    horizontal=True,
)

if key_choice == "Your Key":
    OPENAI_API_KEY = st.sidebar.text_input(
        "First, enter your OpenAI API key", type="password"
    )

elif key_choice == "Free Key (capped)":
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# end::setup[]

# tag::session[]
# Set up Session State
if "messages" not in st.session_state:
    bot_prompt = """
Welcome to the Movie Assistant Chatbot!  
I'm here to assist you with all things movies. Feel free to ask any movie-related questions, and I'll provide you with the information you're looking for. Whether it's details about actors, popular movies, or recommendations based on your preferences – I've got you covered. Let's dive into the world of cinema together! 🎬🤖
"""
    st.session_state.messages = [
        {"role": "assistant", "content": bot_prompt},
    ]
# end::session[]

# tag::submit[]
# Submit handler


def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner('Thinking...'):
        response = generate_response(message)
        write_message('assistant', response)
# end::submit[]


# tag::chat[]
# Display messages in Session State
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message('user', prompt)

    # Generate a response
    handle_submit(prompt)
# end::chat[]
