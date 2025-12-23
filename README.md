# Multilingual FAQ Retrieval Assistant

This project implements a simple multilingual FAQ retrieval assistant that helps users quickly find relevant answers from a knowledge base. This project demonstrates semantic search using sentence embeddings and cosine similarity, enabling natural language queries to retrieve the most appropriate responses.

The assistant supports:
- English and Macedonian queries with automatic translation
- Confidence scoring for answers (High / Medium / Low)
- Real-time question retrieval from a small FAQ dataset
- Session-based conversational memory to display ongoing interactions


## Demo
You can try the FAQ Retrieval Assistant live at:
[**Live Demo**](https://multilingual-faq-retrieval-assistant.streamlit.app/)

### Screenshots

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/2db279c2-cdc0-438a-8b9f-e1f65726a55e" />
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/f3263c95-272d-4032-8379-2dd2eefdbfe2" />

## How It Works

1. A small FAQ dataset (questions and answers) is loaded from a CSV file.
2. All FAQ questions are converted into vector embeddings using a multilingual Sentence Transformer model.
3. When a user asks a question:
   - The question is embedded using the same model.
   - Cosine similarity is calculated between the user question and all FAQ questions.
   - The most similar FAQ question is selected.
4. If the similarity score is high enough, the corresponding answer is returned. Otherwise, a fallback message is shown.
5. Automatically translate answers to Macedonian if selected and show a confidence score.

## Technologies Used
- Python
- Streamlit (UI)
- Sentence-Transformers (Multilingual MiniLM)
- Cosine Similarity
- Pandas
- Google Translator API

## Structure 
```
faq_retrieval_assistant/
│
├── data/
│   └── faq_dataset.csv
│   └── generate_dataset.csv
├── src/
│   ├── app.py
│   └── functions.py
├── requirements.txt
├── README.md
└── .gitignore
```


## Prerequisites
- **Python 3.10+** : Ensure you have Python installed.You can download it from [python.org](https://www.python.org/).

## How to run the project

1. Clone this repository:
```bash
git clone https://github.com/IvaKostadinovaa/faq_retrieval_assistant
```

```bash
cd faq_retrieval_assistant
```

3. **(Optional) Create and activate a virtual environment**  
Open your terminal or command prompt, navigate to the root directory of the project.  
The environment will be created in a local folder named `.venv`.

    3.1 **Create the environment:**
    ```bash
    python -m venv .venv
    ```

    3.2 **Activate the virtual environment:**
    - On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```
    - On Windows:
    ```bash
    .venv\Scripts\activate
    ```

   
4. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
cd src
```
```bash
streamlit run app.py
```
5. App will open at:
```bash
http://localhost:8501
```


### Future UI/UX Enhancements
**Proactive suggested questions**
After an answer is returned, the system could suggest related follow-up questions based on similar FAQs. This would help users continue the conversation more easily, reduce friction, and improve the overall support experience.

**Voice-to-text support**
Voice-to-text input could be integrated to improve accessibility and allow hands-free interaction, which would be especially useful for mobile users.



