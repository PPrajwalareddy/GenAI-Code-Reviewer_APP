import google.generativeai as genai
import streamlit as st

# Read the API key and setup a Gemini client
f = open("gemini.txt")
key = f.read()

genai.configure(api_key=key)

st.markdown("<h1 style='color:Brown;'>GenAI-App : AI Code Reviewer</h1>", unsafe_allow_html=True)
# st.subheader("Python Code Reviewer and Bug Fixer")

# client = GeminiAPI(api_key=GEMINI_API_KEY)

# Take user's input
prompt = st.text_area("Enter your Python code", height=100)

# If button is clicked, generate responses
if st.button("Get Review"):
    st.markdown("<h2 style='color:black;'>Review:</h2>", unsafe_allow_html=True)

    # Original Code
    st.markdown("<h3 style='color:green;font-size:20px;'>Original Code:</h3>", unsafe_allow_html=True)
    st.code(prompt, language='python')

    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest", 
                              system_instruction="""You are a helpful AI Assistant. Given a Python code snippet, you will review it for potential bugs and suggest fixes.""")

    response = model.generate_content(prompt)

    # Display corrected code
    corrected_code = response.text
    st.markdown("<h3 style='color:green;font-size:20px;'>Corrected Code and review:</h3>", unsafe_allow_html=True)
    st.write(corrected_code)
