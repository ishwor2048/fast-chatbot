# import necessary libraries and modules
import os
from dotenv import load_dotenv
import streamlit as st

from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# initialize the api key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# setup prompt (chatbot personality and behavior)
system_prompt = """You are a helpful assistant that provides concise and accurate information. 
If you do not know the answer to a question, respond with 'I don't know'. 
"""

# Utility function to call LLM
def chat_with_llm(user_message):
    response = client.chat.completions.create(
        model = "gpt-4o-mini", 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ], 
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

# streamlit UI setup for a simple frontend chatbot
st.title("Chatbot with OpenAI GPT-4o-mini")

# keep chat history in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# display previous messages 
for role, text in st.session_state["messages"]:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(text)
    
# chat input (bottom)
user_input = st.chat_input("Type your message here...")

if user_input:
    # show user message in chat
    st.session_state["messages"].append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)


    # get response from LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = chat_with_llm(user_input)
            st.markdown(answer)
    
    st.session_state["messages"].append(("assistant", answer))


# THank you for watching this video!! Please hit like and subscrie my youtune channel data speaks!!!