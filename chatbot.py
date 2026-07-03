import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load the API key from the .env file
load_dotenv()

# Initialize the Gemini Client
# It automatically reads the GEMINI_API_KEY from your .env file
client = genai.Client()

# Set up the webpage layout
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Simple Gemini Chatbot")
st.caption("Powered by Gemini 2.5 Flash")

# Initialize chat history in session state so it remembers the conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Redraw all previous messages every time the app reruns
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Wait for user input
if user_input := st.chat_input("Ask me anything..."):
    # 1. Display user message in chat message container
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Display assistant response in chat message container
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        try:
            # Call the Gemini API using the latest SDK and standard flash model
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_input
            )
            bot_response = response.text
            
            # Render the response on the screen
            response_placeholder.markdown(bot_response)
            
            # Save assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            
        except Exception as e:
            error_msg = f"Error communicating with Gemini API: {str(e)}"
            response_placeholder.error(error_msg)