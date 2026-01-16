import chromadb
import requests
from sentence_transformers import SentenceTransformer

DB_PATH = "embeddings"
LM_STUDIO_URL = "http://localhost:1234/v1/completions"

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Chroma (auto-persisted DB)
client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=DB_PATH
    )
)

collection = client.get_or_create_collection(name="flutter_docs")

def ask(question: str):
    # Embed the question
    q_embedding = embed_model.encode([question]).tolist()

    # Retrieve relevant docs
    results = collection.query(
        query_embeddings=q_embedding,
        n_results=4
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
You are a Flutter tutor.
Teach step by step.
Use simple language.
Always include a short Dart example.
Avoid advanced topics unless asked.

Context:
{context}

Question:
{question}
"""

    response = requests.post(
        LM_STUDIO_URL,
        json={
            "model": "local-model",
            "prompt": prompt,
            "max_tokens": 600,
            "temperature": 0.2
        }
    )

    data = response.json()

    if "choices" in data:
        print("\n" + data["choices"][0]["text"].strip() + "\n")
    else:
        print("LM Studio did not return a valid response.")

# Chat loop
print("Flutter tutor ready. Type your question. Ctrl+C to exit.\n")

while True:
    q = input("Flutter > ")
    if not q.strip():
        continue
    ask(q)
