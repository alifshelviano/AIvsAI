# AIvsAI

Compare answers from Gemini and Meta-Llama (OpenRouter) using a simple Streamlit app.

## How to run

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Add your API keys to a `.env` file:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

3. Start the app:
   ```
   streamlit run AIvsAI.py
   ```

## What it does

- Enter a prompt.
- See responses from Gemini and Meta-Llama side by side.