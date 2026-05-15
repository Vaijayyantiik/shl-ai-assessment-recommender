# SHL AI Conversational Assessment Recommendation System

## Overview

This project is an AI-powered conversational recommendation system that helps recruiters discover suitable SHL assessments based on hiring requirements.

The system uses:
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Sentence Transformers
- FAISS Vector Search
- Gemini AI
- FastAPI Backend
- SQLite Database
- Modern Frontend UI

The chatbot understands natural language hiring requirements and recommends relevant SHL assessments with AI-generated reasoning.

---

# Features

## Conversational AI
- Natural language interaction
- Multi-turn conversations
- Clarification handling for vague queries

## Semantic Search
- SentenceTransformer embeddings
- FAISS vector similarity search
- Hybrid retrieval pipeline

## AI Reasoning Layer (RAG)
- Gemini AI integration
- Context-aware recommendations
- Intelligent explanation generation

## Database Integration
- SQLite database
- Chat history storage
- Recommendation logging

## Modern Frontend
- Responsive UI
- Loading spinner
- Timestamps
- Assessment badges
- Interactive recommendation cards

---

# Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

## AI / NLP
- SentenceTransformers
- FAISS
- Gemini API
- Retrieval-Augmented Generation (RAG)

## Frontend
- HTML
- CSS
- JavaScript

---

# System Architecture

```text
User Query
   ↓
Frontend UI
   ↓
FastAPI Backend
   ↓
Retriever
   ↓
FAISS Vector Search
   ↓
Top Assessments
   ↓
Gemini AI Reasoning
   ↓
Final AI Response
```

---

# Folder Structure

```text
shl-agent/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── retrieval/
│   ├── services/
│   └── main.py
│
├── data/
│
├── frontend/
│   └── index.html
│
├── vectorstore/
│
├── README.md
│
└── requirements.txt
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd shl-agent
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Gemini API

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

---

# Generate Embeddings

```bash
python app/retrieval/embedder.py
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

---

# Open Frontend

```bash
start frontend/index.html
```

---

# Example Queries

- Need assessment for Python backend engineer
- Looking for leadership and communication evaluation
- Need finance and bookkeeping assessment
- Hiring Java developer with problem-solving skills

---

# Future Improvements

- Authentication system
- User sessions
- Cloud deployment
- Redis caching
- Advanced reranking models
- Multi-user support
- Analytics dashboard

---

# Author

Vaijayanti Kulkarni

---

# License

This project is for educational and assignment purposes.
