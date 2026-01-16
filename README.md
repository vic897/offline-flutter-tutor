# Offline Flutter Tutor (Local LLM + RAG)

An offline Flutter learning assistant that uses official Flutter documentation and a locally running large language model to explain concepts, debug errors, and guide Flutter app development — without relying on an internet connection.

This project was built to enable focused learning, avoid hallucinated answers, and reduce dependency on online tutorials and forums.

---

## Features

- Uses curated Flutter documentation as the knowledge source  
- Retrieval-Augmented Generation (RAG) for accurate, context-based answers  
- Fully offline after initial setup  
- Command-line interface for distraction-free usage  
- Step-by-step explanations with simple Dart examples  

---

## Tech Stack

- **Python** – core implementation  
- **ChromaDB** – vector database for document retrieval  
- **Sentence-Transformers** – text embeddings  
- **LM Studio** – local LLM inference server  
- **RAG (Retrieval-Augmented Generation)** – grounding model responses in real docs  

---

## Project Structure


flutter-tutor/
├── docs_clean/ # Curated Flutter documentation in Markdown
├── embeddings/ # Vector database (generated during ingestion)
├── ingest.py # One-time document ingestion script
├── chat.py # CLI-based Flutter tutor
├── README.md
└── .gitignore

---


---

## How It Works

1. Flutter documentation is manually selected and cleaned.
2. Documents are split into small chunks and converted into embeddings.
3. Embeddings are stored in a local ChromaDB vector database.
4. User questions are embedded and matched against relevant documentation.
5. Retrieved context is sent to a local LLM running in LM Studio.
6. The model responds using only the provided Flutter documentation.

---

## Setup Instructions

### 1. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install chromadb sentence-transformers requests
```

### 3. Ingest Flutter documentation (one-time step)
```bash
python ingest.py
```

This builds the local vector database.


### 4. Start LM Studio

1. Load an instruct-style model (e.g., Mistral, Qwen)
2. Enable Local Server
3. Note the server port (default: 1234)


### 5. Run the Flutter tutor
```bash
python chat.py
```


### Example Queries
Explain StatelessWidget vs StatefulWidget
Why does setState rebuild the widget tree?
Explain this Flutter error: <paste error>
Give me a small practice task on Row and Column


### Why This Project

## This project was built to:

Learn Flutter using official documentation instead of shallow tutorials
Prevent hallucinated or incorrect explanations from LLMs
Explore practical use of RAG systems and local LLM tooling
Build a reusable developer-focused learning assistant


## Limitations

Documentation must be manually curated
Not a replacement for full API references
CLI-only by design (no GUI)


## Future Improvements

Automatic documentation ingestion
Error-focused debugging mode
Interactive quizzes and practice tasks
Optional TUI or web interface
