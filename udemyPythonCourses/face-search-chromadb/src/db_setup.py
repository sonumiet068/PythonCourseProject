import chromadb
from chromadb import PersistentClient 

def get_chroma_collection():
  client = chromadb.PersistentClient(path="./face_db")
  return client.get_or_create_collection(name="faces",metadata={"hnsw:space": "cosine"})



 




