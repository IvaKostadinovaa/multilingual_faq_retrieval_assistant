import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from deep_translator import GoogleTranslator


@st.cache_data
def dataset_loading(path):
    try:
        df = pd.read_csv(path)
        questions = df["question"].tolist()
        answers = df["answer"].tolist()
        return questions, answers
    except FileNotFoundError:
        st.error("Dataset not found")
        return [], []

@st.cache_resource
def model_loading():
    try:
     model= SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
     return model
    except:
        st.error("Model not found")
        return None

@st.cache_data
def questions_embedding(_model, questions):
    return _model.encode(questions, convert_to_tensor=True)

def user_question_embedding(model, question):
    return model.encode(question, convert_to_tensor=True)

def retrieve_top_k(embedded_questions,embedded_user_question,k=3):
    cosine_score = util.cos_sim(embedded_questions, embedded_user_question).squeeze()
    top_results = cosine_score.topk(k=k)
    return top_results

def confidence_label(score):
    if score>=0.7:
        return "High"
    elif score>= 0.5:
        return "Medium"
    else:
        return "Low"


def translate(answer, language_choice):
    if language_choice == "Macedonian":
        try:
         return GoogleTranslator(source="en", target="mk").translate(answer)
        except:
         return answer
    return answer


def best_answer(top_results, answers, language_choice):
    best_idx = top_results.indices[0]
    best_score = float(top_results.values[0])

    if best_score < 0.5:
        message = "Sorry, we couldn't find relevant answer to your question. Please try rephrasing your question or contact support."
        final_text = translate(message, language_choice)
    else:
        final_text = translate(answers[best_idx], language_choice)

    confidence = confidence_label(best_score)

    return best_idx, best_score, final_text, confidence
