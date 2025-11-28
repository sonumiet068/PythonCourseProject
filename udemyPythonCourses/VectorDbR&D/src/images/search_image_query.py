import os
import emoji
import imagemodel
import embedding_ops
import chroma_db_connections
import load_image_chromadb


# processor = CLIPProcessor.from_pretrained(model_name,use_fast=True)
#--------Step 1: Connect to chroma ----------------
collection = chroma_db_connections.get_chroma_db_connection("image_vectors")
#--------- Step 2:  insert images --------------------
load_image_chromadb.load_image("/Users/sonuLocalDrive/my_images/image_search/",collection)

query_image_path = "/Users/sonuLocalDrive/my_images/image_search/QueryImages/Shraddha_Kapoor_2016.jpg"
query_vector = embedding_ops.get_image_embedding(query_image_path)
results = collection.query(query_embeddings=[query_vector],n_results=2)
print(f"Search Results : {results}")





