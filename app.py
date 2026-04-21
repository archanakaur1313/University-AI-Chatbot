import streamlit as st
from datetime import datetime
import antigravity

# 1. Page Config (Dark Mode / Title)
st.set_page_config(page_title="AutoMechanic AI", layout="centered")

# 2. Time Training Logic
now = datetime.now()
current_time = now.strftime("%H:%M")
current_date = now.strftime("%B %d, %Y")

# 3. Sidebar / Header
st.title("🔧 AutoMechanic AI")
st.caption(f"Currently in the Garage | {current_date} {current_time}")

# 4. Initialize Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Logic
if prompt := st.chat_input("Ask about your engine, oil, or brakes..."):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # "Training" the AI with Time Context
    system_instruction = f"You are a helpful AutoMechanic AI. The time is {current_time}. Be energetic if it's day, and remind users the physical shop is closed if it's after 6 PM."

    # Generate Response via Antigravity
    # (Using a placeholder logic for the demo, replace with your specific Antigravity call)
    try:
        response = f"I see you're asking about '{prompt}'. Since it's {current_time}, I'd recommend checking your oil levels before the sun goes down!"
        # In your real code, you'd use: response = antigravity.query(prompt, context=system_instruction)
    except:
        response = "I'm having a bit of engine trouble connecting to my brain. Try again in a second!"

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
