import streamlit as st
from functions import *
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "data", "faq_dataset.csv")


language_choice = st.selectbox(
    "Select language / Избери јазик :",
    ["English", "Macedonian"]
)

questions, answers = dataset_loading(DATASET_PATH)
if not questions or not answers:
    st.stop()

model = model_loading()
if model is None:
    st.stop()

embedded_questions = questions_embedding(model, questions)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if language_choice == "Macedonian":
    input_prompt = "Постави прашање..."
else:
    input_prompt = "Ask us a question..."

prompt = st.chat_input(input_prompt)

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    embedded_user = user_question_embedding(model, prompt)
    top_results = retrieve_top_k(embedded_questions, embedded_user)
    best_idx, score, best_answer_text, confidence = best_answer(top_results, answers, language_choice)

    assistant_text = (
        f"{best_answer_text}\n\n"
        f"*Confidence: {confidence} ({score:.2f})*"
    )


    with st.chat_message("assistant"):
        st.markdown(assistant_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_text}
    )

