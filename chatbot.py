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
.stChatMessage {
    border-radius: 12px;
    margin-bottom: 10px;
    padding: 14px;
    border: 1px solid #262730;
}
code {
    color: #ff79c6 !important;
    background-color: #1e1e24 !important;
    padding: 2px 6px;
    border-radius: 4px;
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
    if st.button("🔄 Clear App Context Cache", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.success("✨ Active Brain Module: Gemini 2.5 Flash")
    st.divider()
    st.info("💡 Project Status: Operational Layer Active")
    st.write("### 🧭 Core App Blueprint")
    st.markdown("""
    1️⃣ **Input Layer:** Receives text snippets  
    2️⃣ **API Pipeline:** Direct Gemini flash token routing  
    3️⃣ **State Engine:** Persistent session mapping  
    """)

# Initialize state engine trackers
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask me anything..."):
    # 1. Save and display the user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. Process assistant response
    with st.chat_message("assistant"):
        # Create the loading container
        with st.status("SimpleExplainer is thinking...", expanded=True) as status:
            try:
                # Call the Gemini API
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input
                )
                bot_response = response.text
                
                # Automatically complete and collapse the status box
                status.update(label="Response Generated", state="complete", expanded=False)
                
            except Exception as e:
                status.update(label="Generation Failed", state="error", expanded=True)
                st.error(f"Error communicating with Gemini API: {str(e)}")
                bot_response = None

        # 3. Output response text automatically outside the loader box
        if bot_response:
            st.markdown(bot_response)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})


st.divider()
st.caption("⚡ SimpleExplainer.AI Dashboard Pipeline • Engineered under Streamlit Core Optimization Ecosystem")