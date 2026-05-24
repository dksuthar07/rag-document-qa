# RAG-Powered Document Q&A System

AI-powered application that allows users to upload multiple documents and ask contextual questions using Retrieval-Augmented Generation (RAG).

---

## Problem Statement

Professionals waste hours manually searching lengthy documents for specific answers.

This project solves that problem by enabling semantic document retrieval and natural language question answering.

---

## Features

- Multi-Document Upload
- PDF & DOCX Support
- Semantic Search
- RAG Pipeline
- HuggingFace Embeddings
- FAISS Vector Database
- Groq LLM Integration
- Source Citations
- Chat Interface
- Streamlit UI
- Cloud Deployment

---

## Tech Stack

| Layer | Technology |
|-------|------|
| Frontend | Streamlit |
| Framework | LangChain |
| Embeddings | Sentence Transformers |
| Vector DB | FAISS |
| LLM | Groq |
| Model | Llama 3.3 |
| Deployment | Streamlit Cloud |

---

## Architecture

User Uploads Documents
↓
Loader
↓
Chunking
↓
Embeddings
↓
FAISS Vector Database
↓
Retriever
↓
Groq LLM
↓
Answer Generation

---

## Installation

```bash
git clone YOUR_REPO_URL
cd rag-document-qa
```

Create environment:

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Deployment

Deployed using Streamlit Cloud.

---

## Future Improvements

- Conversation Memory
- Hybrid Search
- OCR Support
- Persistent Vector Database
- Authentication


## Architecture Diagram
                ┌────────────────────┐
                │ User Upload Files  │
                └──────────┬─────────┘
                           │
                           ▼
               ┌──────────────────────┐
               │ PDF / DOCX Loader    │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ Text Chunking        │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ HF Embeddings        │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ FAISS Vector Store   │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ Retriever            │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ Groq LLM             │
               └──────────┬───────────┘
                          │
                          ▼
               ┌──────────────────────┐
               │ Contextual Answer    │
               └──────────────────────┘
