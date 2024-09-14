# chatbot/main.py

import ollama
from config import Config

# Define the system prompt
system_prompt = Config.SYSTEM_PROMPT

# Function to send a user prompt and stream the response
def chat(user_prompt, model):
    """
    Sends the user prompt to the selected model and streams the response.
    """
    stream = ollama.chat(
        model=model,
        messages=[{'role': 'assistant', 'content': system_prompt},
                  {'role': 'user', 'content': f"Model being used is {model}.{user_prompt}"}],
        stream=True
    )
    return stream

# Function to handle the streaming response
def stream_parser(stream):
    """
    Parses the stream response and yields chunks of the LLM response.
    """
    for chunk in stream:
        yield chunk['message']['content']
