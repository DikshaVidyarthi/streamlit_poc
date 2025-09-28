# app.py
import streamlit as st
from datetime import datetime

# Title of the app
st.title("Welcome to My First Streamlit App!")

# User input
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)

# Button to submit
if st.button("Submit"):
    if name:
        birth_year = datetime.now().year - age
        st.success(f"Hello {name}! You were born in {birth_year}.")
    else:
        st.error("Please enter your name.")