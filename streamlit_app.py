#!/usr/bin/env python3
# streamlit_app.py
"""
Streamlit Chat UI for the Coffee Shop FAQ Chatbot.
Run with: streamlit run streamlit_app.py
"""

import streamlit as st
from coffee_chatbot import get_reply

st.set_page_config(page_title="Coffee Shop Chatbot", page_icon="☕")

st.title("☕ Coffee Shop FAQ Chatbot")

# Initialize chat history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        # Get bot reply
        bot_reply = get_reply(user_input)
        # Save messages
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", bot_reply))
        # Clear input
        st.session_state.input = ""

# Display conversation
for speaker, message in st.session_state.history:
    if speaker == "You":
        st.markdown(
            f"<div style='text-align: right; background-color:#DCF8C6; padding:8px; border-radius:8px; margin:4px;'>**You:** {message}</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(
            f"<div style='text-align: left; background-color:#FFF; padding:8px; border-radius:8px; margin:4px;'>**Bot:** {message}</div>",
            unsafe_allow_html=True)
