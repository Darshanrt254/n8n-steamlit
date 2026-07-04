import streamlit as st
import requests

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Personal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

/* Main Container */
.block-container {
    padding-top: 2rem;
    max-width: 900px;
}

/* Header */
.title {
    margin-top: 80px !important;
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #38bdf8;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

/* Chat input */
.stChatInput {
    position: fixed;
    bottom: 20px;
    width: 60%;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.markdown("### Capabilities")

    st.markdown("""
✅ Answer Questions

📅 Manage Calendar

📧 Read & Send Emails

📝 Notes & Tasks

💰 Expense Tracking

⚡ AI Automation
""")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------- HEADER --------------------
st.markdown('<p class="title">🤝 Personal AI Assistant</p>',
            unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Your intelligent assistant powered by n8n + AI</p>',
    unsafe_allow_html=True
)

# -------------------- SESSION --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Welcome message
if len(st.session_state.messages) == 0:
    st.info("👋 Hello! Ask me anything...")

# -------------------- DISPLAY CHAT --------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------- CHAT INPUT --------------------
user_message = st.chat_input("Type your message...")

if user_message:

    # Show User Message
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    with st.chat_message("user"):
        st.markdown(user_message)

    # Loading Animation
    with st.spinner("Thinking..."):

        response = requests.post(
            "https://darshan-rt25406.app.n8n.cloud/webhook/851de76e-fdc4-4ebb-b3d0-31e5263d10b0",
            json={"message": user_message}
        )

        ai_response = response.json()[0]["output"]

    # Display Assistant Response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )

    with st.chat_message("assistant"):
        st.markdown(ai_response)