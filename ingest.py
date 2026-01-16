import os
from sentence_transformers import SentenceTransformer
import chromadb

DOCS_PATH = "docs_clean"
DB_PATH = "embeddings"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=DB_PATH
    )
)

collection = client.get_or_create_collection(name="flutter_docs")

docs = []
metas = []
ids = []

i = 0
for file in os.listdir(DOCS_PATH):
    if file.endswith(".md"):
        with open(os.path.join(DOCS_PATH, file), "r", encoding="utf-8") as f:
            text = f.read()

        chunks = [text[j:j+500] for j in range(0, len(text), 450)]
        for chunk in chunks:
            docs.append(chunk)
            metas.append({"source": file})
            ids.append(str(i))
            i += 1

embeddings = model.encode(docs).tolist()

collection.add(
    documents=docs,
    metadatas=metas,
    embeddings=embeddings,
    ids=ids
)


print("Ingestion complete. Flutter brain is ready.")
