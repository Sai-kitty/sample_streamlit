# Save this as app.py
import streamlit as st

# Title of the app
st.title("Hello, Streamlit!")

# Input and output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
