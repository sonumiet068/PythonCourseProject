import os
import chromadb

def get_chroma_db_connection(db_name="image_vectors"):
  client = chromadb.Client()
  return client.create_collection(
    name= db_name
  )