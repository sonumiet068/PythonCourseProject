from db_setup import get_chroma_collection
from camera_capture import capture_from_camera
from embedder import get_embedding_from_image

collection = get_chroma_collection()

print("Captutre a face to search from chromadb")

img = capture_from_camera("Search mode")
if img is None:
  print("No image is captured!")
  exit()

embedding =  get_embedding_from_image(image=img)

results = collection.query(query_embeddings=[embedding],n_results=1)
print(results)




