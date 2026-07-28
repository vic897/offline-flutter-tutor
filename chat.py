import chromadb
import requests
from sentence_transformers import SentenceTransformer

DB_PATH = "embeddings"
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to persistent Chroma database
client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(name="flutter_docs")

print(f"Loaded {collection.count()} document chunks.\n")


def ask(question: str):
    # Embed the question
    q_embedding = embed_model.encode([question]).tolist()

    # Retrieve relevant documentation
    results = collection.query(
        query_embeddings=q_embedding,
        n_results=4
    )

    if not results["documents"] or len(results["documents"][0]) == 0:
        print("No relevant documentation found.")
        return

    context = "\n\n".join(results["documents"][0])

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert Flutter tutor.\n"
                "Answer ONLY using the provided documentation.\n"
                "Teach step by step.\n"
                "Use simple language.\n"
                "Always include a short Dart example.\n"
                "If the documentation does not contain the answer, clearly say so."
            )
        },
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{question}
"""
        }
    ]

    response = requests.post(
        LM_STUDIO_URL,
        json={
            "model": "qwen2.5-coder-7b-instruct",
            "messages": messages,
            "temperature": 0.2,
            "max_tokens": 1200
        }
    )

    if response.status_code != 200:
        print("\nLM Studio Error:")
        print(response.text)
        return

    data = response.json()

    if "choices" not in data:
        print("\nUnexpected response:")
        print(data)
        return

    answer = data["choices"][0]["message"]["content"]

    print("\n" + "=" * 80)
    print(answer)
    print("=" * 80 + "\n")


print("Flutter Tutor Ready!")
print("Type 'exit' to quit.\n")

while True:
    question = input("Flutter > ").strip()

    if question.lower() in ["exit", "quit"]:
        break

    if question == "":
        continue
    ask(question)