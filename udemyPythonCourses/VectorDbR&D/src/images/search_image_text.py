import os
import emoji
import imagemodel
import embedding_ops
import chroma_db_connections
import load_image_chromadb

#--------Step 1: Connect to chroma ----------------
collection = chroma_db_connections.get_chroma_db_connection("image_vectors")
#--------- Step 2:  insert images --------------------
load_image_chromadb.load_image("/Users/sonuLocalDrive/my_images/image_search/",collection)

#Search Query with Text
text_query ="cat with flower crown"
query_vector = embedding_ops.get_text_embedding(text_query)
results=collection.query(query_embeddings=[query_vector],n_results=2)
print(results)