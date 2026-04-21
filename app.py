import streamlit as st
from chat import get_ai_response # This connects the two files!

# 1. Page Config
st.set_page_config(page_title="AutoMechanic AI", layout="centered")

# 2. Styling (Matching your Dark Aesthetic)
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

    # Get response from our 'chat.py' brain
    ai_response = get_ai_response(prompt)

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})    try:
        response = f"I see you're asking about '{prompt}'. Since it's {current_time}, I'd recommend checking your oil levels before the sun goes down!"
        # In your real code, you'd use: response = antigravity.query(prompt, context=system_instruction)
    except:
        response = "I'm having a bit of engine trouble connecting to my brain. Try again in a second!"

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
