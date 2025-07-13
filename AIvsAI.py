import streamlit as st
import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv

# --- Load keys from .env ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = "meta-llama/llama-3-8b-instruct"

# --- Configure Gemini ---
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

# --- Streamlit UI ---
st.set_page_config(page_title="Gemini vs Meta-LLama", layout="centered")
st.title("🤖 Gemini vs Meta-LLama (OpenRouter)")

prompt = st.text_area("Enter your prompt", height=100)

if st.button("Ask Both AIs"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        # --- Gemini Response ---
        with st.spinner("Gemini thinking..."):
            try:
                gemini_response = gemini_model.generate_content(prompt)
                gemini_text = gemini_response.text
            except Exception as e:
                gemini_text = f"❌ Gemini Error: {e}"

        # --- Mistral via OpenRouter ---
        with st.spinner("Meta-LLama thinking..."):
            try:
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": OPENROUTER_MODEL,
                        "messages": [{"role": "user", "content": prompt}],
                    }
                )
                mistral_text = response.json()["choices"][0]["message"]["content"]
            except Exception as e:
                mistral_text = f"❌ Mistral Error: {e}"

        # --- Display ---
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🤖 Gemini")
            st.write(gemini_text)

        with col2:
            st.markdown("### 🧠 Meta-LLama via OpenRouter")
            st.write(mistral_text)
