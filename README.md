# CodeConvert 

**CodeConvert** is an online code conversion tool powered by Hugging Face's Mistral-7B model, designed to translate code from one programming language to another efficiently. This application is built with Python using the Streamlit library to provide a simple and interactive web-based interface for developers.

---

## Features

- **Multi-language Conversion**: Converts code between popular programming languages, including:
  - Source: COBOL, Python, Java, JavaScript, Ruby
  - Target: C++, Python, Java, JavaScript, Ruby
- **High Accuracy**: Estimates conversion accuracy dynamically.
- **Streamlined Interface**: A user-friendly form to input source code, select the source and target languages, and display the output.

---

## How It Works

1. Select the **Source Language** and provide the code you wish to convert in the text area.
2. Choose the desired **Target Language**.
3. Hit the `Convert` button to process your code.
4. View the converted code output and the estimated accuracy score.

The tool communicates with the Hugging Face's Mistral-7B-Instruct model to generate the converted code.

---

## Requirements

### Prerequisites
- Python 3.9 or later.
- Installed Python packages from `requirements.txt`:
  ```text
  streamlit==1.x
  huggingface_hub==x.x.x
  ```
- Hugging Face access token for model usage (ensure the `InferenceClient` uses a valid token).

---

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd CodeConvert
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```


## Code Conversion Model

This app uses [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) hosted on Hugging Face. The model is integrated via the `huggingface_hub` library and provides real-time streaming output for code conversion.

### Conversion Accuracy
A placeholder function simulates accuracy for demonstration purposes. Future iterations will include rigorous evaluation of output using specific code correctness checks.

---

## Usage Instructions

1. **Source Language and Code**:
   - Choose the source programming language.
   - Enter the code you want to convert into the input field.
   
2. **Target Language**:
   - Select the target programming language.

3. **Code Conversion**:
   - Click `Convert` to process your input code.

4. **View Results**:
   - The converted code will display on the right panel.
   - The estimated accuracy will show below the converted code.

---

## Troubleshooting

- **Model Overload**: 
  - If the Hugging Face server is overloaded, the app retries conversion with exponential backoff. 
  - If retries fail, an error message suggests trying later.
  
- **Code Errors**:
  - Check the source and target code syntax; this tool assumes standard language syntax.

---

## Future Enhancements

- Implement actual accuracy calculation.
- Expand supported languages for conversion.
- Add testing and debugging options for converted code.
- Offline mode using local deployment of models.

---

## Acknowledgments

Special thanks to:
- [Streamlit](https://streamlit.io) for making web app development straightforward.
- [Hugging Face](https://huggingface.co) for providing state-of-the-art models and hosting solutions.

---
