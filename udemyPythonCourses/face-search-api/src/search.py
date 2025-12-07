import chromadb
import os
from src.embedder import get_face_embedding
from PIL import Image
import numpy as np

os.environ["CHROMA_TELEMETRY_DISABLED"] = "1"

client = chromadb.PersistentClient(path="db")
collection = client.get_or_create_collection(
    "faces",
    metadata={"hnsw:space": "cosine"}
)

def add_face(image_path, person_id):
    image = np.array(Image.open(image_path))
    emb, _ = get_face_embedding(image)

    if emb is None:
        return False, "No face detected!"

    collection.add(
        ids=[person_id],
        embeddings=[emb],
        metadatas=[{"image_path": image_path}]
    )
    return True, "Face added."

def search_face(image_path, top_k=1):
    image = np.array(Image.open(image_path))
    emb, _ = get_face_embedding(image)

    if emb is None:
        return None

    result = collection.query(
        query_embeddings=[emb],
        n_results=top_k
    )
    return result
