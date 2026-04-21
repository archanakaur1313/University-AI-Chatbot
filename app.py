import streamlit as st
from chatbot import get_ai_response # Points to your chatbot.py file

# 1. Page Config
st.set_page_config(page_title="AutoMechanic AI", layout="centered")

# 2. Styling (Dark Aesthetic)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    </style>
    """, unsafe_allow_status=True)

st.title("🔧 AutoMechanic AI")
st.caption("University Gen AI Project | Interactive Mechanic Assistant")

# 3. Initialize Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input Logic
if prompt := st.chat_input("Ask about your engine, oil, or brakes..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from our 'chatbot.py' brain
    try:
        ai_response = get_ai_response(prompt)
    except Exception as e:
        ai_response = "I'm having a bit of engine trouble. Try again!"

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    
    # Save to memory
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})        ai_response = "I'm having a bit of engine trouble connecting to my brain. Try again!"

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
