import streamlit as st
from happytransformer import HappyTextToText, TTSettings

# Initialize the grammar correction model
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)

# Streamlit App
st.title("Grammar Correction Tool")

# Input box for the user to enter text
input_text = st.text_area("Enter text to correct:", "")

# Button to trigger grammar correction
if st.button("Correct Grammar"):
    if input_text:
        # Add the prefix "grammar: " before the input text
        result = happy_tt.generate_text("grammar: " + input_text, args=args)
        st.write("Corrected Text:")
        st.write(result.text)
    else:
        st.write("Please enter some text to correct.")
