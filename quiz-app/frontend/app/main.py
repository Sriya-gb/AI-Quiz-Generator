import streamlit as st
import requests
import quiz_generator 

st.title("AI-Powered Quiz Generator")

text_input = st.text_area("Enter your text here:")
num_questions = st.number_input("Number of questions to generate:", min_value=1, max_value=10, value=5)

if st.button("Generate Quiz"):
    if text_input:
        with st.spinner("Generating quiz..."):
            quiz = quiz_generator.generate_quiz(text_input, num_questions)
        st.text_area("Generated Quiz:", quiz, height=400)
    else:
        st.warning("Please enter some text to generate a quiz.")

