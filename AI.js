import axios from 'axios';
import OpenAI from 'openai';

const GEMINI_API_KEY = "AIzaSyBxKPDLwh2WFHnECk_hDk_krp2yg_fI_iU";
const OPENAI_API_KEY = "pmpt_685ad0b64d348194ba151adfc6bd7e36066b69e73ca3212f";

// Gemini Setup
const GEMINI_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${GEMINI_API_KEY}`;

// OpenAI Setup
const openai = new OpenAI({
  apiKey: OPENAI_API_KEY,
});

async function askGemini(prompt) {
  try {
    const res = await axios.post(GEMINI_URL, {
      contents: [{ role: 'user', parts: [{ text: prompt }] }],
    });
    return res.data.candidates[0].content.parts[0].text;
  } catch (err) {
    return `❌ Gemini Error: ${err?.response?.data?.error?.message || err.message}`;
  }
}

async function askOpenAI(prompt) {
  try {
    const completion = await openai.chat.completions.create({
      model: 'gpt-4', // or 'gpt-3.5-turbo'
      messages: [{ role: 'user', content: prompt }],
    });
    return completion.choices[0].message.content;
  } catch (err) {
    return `❌ OpenAI Error: ${err?.response?.data?.error?.message || err.message}`;
  }
}

async function compareAI(prompt) {
  console.log(`🧠 Prompt: ${prompt}\n`);

  const [geminiResponse, openaiResponse] = await Promise.all([
    askGemini(prompt),
    askOpenAI(prompt),
  ]);

  console.log(`🤖 Gemini:\n${geminiResponse}\n`);
  console.log(`🧠 OpenAI:\n${openaiResponse}\n`);
}

// Example
const input = "Who would win in a chess match, you or GPT?";
compareAI(input);
