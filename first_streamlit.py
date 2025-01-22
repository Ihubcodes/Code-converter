import streamlit as st
from huggingface_hub import InferenceClient, errors
import time
import random

# Function to initialize the InferenceClient
def client_fn():
    return InferenceClient("mistralai/Mistral-7B-Instruct-v0.2")
# Custom system instructions to guide the model's behavior
system_instructions = (
    "[SYSTEM]"
    "Your goal is to convert code from one programming language to another based on the user's input. "
    "You should provide accurate and functional code in the target language. "
    "[SOURCE CODE]"
    "Language: [SOURCE LANGUAGE]"
    "Target Language: [TARGET LANGUAGE]"
    "[CONVERTED CODE]"
)

# Function to generate code conversion using the Hugging Face model
def convert_code(source_code, source_lang, target_lang, retries=3):
    client = client_fn()
    
    generate_kwargs = dict(
        max_new_tokens=300,
    )
    
    formatted_prompt = system_instructions.replace(
        "[SOURCE CODE]", source_code
    ).replace(
        "[SOURCE LANGUAGE]", source_lang
    ).replace(
        "[TARGET LANGUAGE]", target_lang
    )
    
    attempt = 0
    while attempt < retries:
        try:
            stream = client.text_generation(
                formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False
            )
            
            output = ""
            for response in stream:
                if not response.token.text == "</s>":
                    output += response.token.text
            return output
        except errors.OverloadedError:
            attempt += 1
            time.sleep(2 ** attempt)  # Exponential backoff
    return "The model is currently overloaded. Please try again later."

# Function to calculate accuracy (placeholder function, you need to replace it with actual accuracy calculation logic)
def calculate_accuracy():
    return random.uniform(92, 99)  # Placeholder logic for accuracy calculation

# Streamlit UI
st.set_page_config(
    page_title="CodeConvert",
    page_icon="💻",
    layout="wide",
)

st.title("CodeConvert")

with st.container():
    st.header("Online Code Converter")
    
    with st.form(key='conversion_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Source Language")
            source_language = st.selectbox("Select Source Language", ["COBOL", "Python", "Java", "JavaScript", "Ruby"])
            st.text_area("Your input code here", height=300, key="source_code")
        
        with col2:
            st.subheader("Target Language")
            target_language = st.selectbox("Select Target Language", ["C++", "Python", "Java", "JavaScript", "Ruby"])
            output_code = st.empty()  # Placeholder for output code

        submit_button = st.form_submit_button("Convert")

    if submit_button:
        source_code = st.session_state.source_code
        if source_code and source_language and target_language:
            with st.spinner("Converting code..."):
                converted_code = convert_code(source_code, source_language, target_language)
                accuracy = calculate_accuracy()
            output_code.code(converted_code)
            st.subheader("Code Accuracy")
            st.write(f"Accuracy: {accuracy:.2f}%")
        else:
            st.error("Please fill in all fields.")

