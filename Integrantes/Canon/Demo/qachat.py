from dotenv import load_dotenv

load_dotenv()

import streamlit as st

import os 
import google.generativeai as genai

from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
###

model = genai.GenerativeModel(
  model_name="tunedModels/qa-medicina-lfv3n6oxlayy",
  generation_config=generation_config,
  safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
  }
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="Preguntas de medicina App-demo")

st.header("App de Gemini")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input= st.text_input("Input: ", key='input')
submit=st.button("Realiza una pregunta")

if submit and input:
    response= get_gemini_response(input)

    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("El historial del chat es:")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")