# 📄 Document Chatbot (RAG)

## Overview

Document Chatbot (RAG) is a Streamlit-based application that allows users to upload PDF documents and ask questions about their content. The application uses Retrieval-Augmented Generation (RAG), OpenAI embeddings, and a FAISS vector database to retrieve relevant information from the uploaded document and generate accurate answers.

---

## Features

* Upload PDF documents
* Extract text from PDF files
* Split text into smaller chunks
* Generate embeddings using OpenAI
* Store embeddings in a FAISS vector database
* Retrieve relevant document sections
* Answer questions using GPT-4.1 Mini
* Simple and user-friendly Streamlit interface

---

## Project Structure

```
DocumentChatbot/
│
├── app.py
├── chatbot.py
├── config.py
├── pdf_reader.py
├── vector_store.py
├── requirements.txt
├── .env
└── README.md
```

---

## Technologies Used

* Python
* Streamlit
* LangChain
* LangChain OpenAI
* LangChain Community
* LangChain Text Splitters
* OpenAI API
* FAISS
* PyPDF
* Python Dotenv

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd DocumentChatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Configure OpenAI API Key

Create a `.env` file in the project folder.

```text
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

---

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## How It Works

1. Upload a PDF document.
2. The application extracts text from the PDF.
3. The text is divided into smaller chunks.
4. OpenAI generates embeddings for each chunk.
5. FAISS stores the embeddings.
6. When a user asks a question, the most relevant text chunks are retrieved.
7. GPT-4.1 Mini generates an answer using the retrieved context.

---

## Requirements

* Python 3.10 or above
* OpenAI API Key
* Internet connection

---

## Author

Supriya Reddy

---

## License

This project is developed for educational purposes.
