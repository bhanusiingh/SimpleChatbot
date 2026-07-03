import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environmental configurations
load_dotenv()
client = genai.Client()

# Set up presentation layout
st.set_page_config(page_title="SimpleExplainer.AI", page_icon="🧠", layout="wide", initial_sidebar_state="expanded")

# Inject Custom Branding Styles
st.markdown("""
<style>
html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }
.main { background: #0e1117; }
.hero-header {
    padding: 24px;
    border-radius: 16px;
    background: linear-gradient(135deg, #1e3a8a, #5b21b6);
    color: #ffffff;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Render Hero Banner Element
st.markdown("""
<div class="hero-header">
    <h1>🧠 SimpleExplainer.AI — Chat Workspace</h1>
    <p>A highly responsive educational hub built to parse code syntax models and test conceptual comprehension pipelines.</p>
</div>
""", unsafe_allow_html=True)

# Build Sidebar Architecture
with st.sidebar:
    st.title("📝 Control Panel")
    st.success("✨ Active Brain Module: Gemini 2.5 Flash")
    st.divider()
    st.info("💡 Project Status: Operational Layer Active")

# Initialize state engine trackers
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        try:
            response = client.models.generate_content(model='gemini-2.5-flash', contents=user_input)
            bot_response = response.text
            response_placeholder.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
        except Exception as e:
            response_placeholder.error(f"Error communicating with Gemini API: {str(e)}")

