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

