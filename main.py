import streamlit as st
from services.groq_service import GroqService 
from services.prompt_builder import generate_meta_prompt

groq = GroqService(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(page_title="Text Assembler", layout="centered")

st.title("Prompt Designer")
st.info("PARTS")

# Initialize session state for the result
if "final_text" not in st.session_state:
    st.session_state.final_text = ""

parts = ["Persona","Aim","Recipients","Theme","Structure"]
with st.form("input_form"):
    # Create 5 inputs dynamically using a list comprehension or simple loop

    inputs = []
    for part in parts:
        val = st.text_input(f"{part}", max_chars=250)
        inputs.append(val)
        
    submit = st.form_submit_button("➤",use_container_width=True)

if submit:
    # Filter out empty strings and join with double newlines
    st.session_state.final_text = groq.generate(generate_meta_prompt(inputs))

if st.session_state.final_text:
    st.subheader("Result")
    st.code(st.session_state.final_text, language=None)

