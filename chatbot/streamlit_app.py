# chatbot/streamlit_app.py

import streamlit as st
from config import Config
from main import chat, stream_parser

# Set up the Streamlit page config
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    initial_sidebar_state="expanded"
)

# Title for the app
st.title(Config.PAGE_TITLE)

# Sidebar for model selection
with st.sidebar:
    st.markdown("# Chat Options")
    model = st.selectbox('What model would you like to use?', Config.OLLAMA_MODELS)

# Check if session state has stored messages, if not, initialize it
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages from the session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture user input in the chat widget
if user_prompt := st.chat_input("What would you like to ask?"):
    # Display the user's input in the chat message widget
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Add user's message to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generate a response from the model
    with st.spinner('Generating response...'):
        llm_stream = chat(user_prompt, model=model)
        stream_output = "".join([chunk for chunk in stream_parser(llm_stream)])

        # Display the assistant's response in the chat
        with st.chat_message("assistant"):
            st.markdown(stream_output)

        # Add the assistant's response to the session state
        st.session_state.messages.append({"role": "assistant", "content": stream_output})
