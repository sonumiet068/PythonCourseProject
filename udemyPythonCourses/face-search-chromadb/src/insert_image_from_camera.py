import uuid
from camera_capture import capture_from_camera
from db_setup import get_chroma_collection
from embedder import get_embedding_from_image

collection = get_chroma_collection()
print("Now,Capture a face to INSERT into database")
img = capture_from_camera("Insert mode")

if img is None:
  print("No image captured !")
  exit()

embedding = get_embedding_from_image(img)
if embedding is None:
  print("No face Detected!")
  exit()
name = input("Enter person name:")

face_id = f"{name}_{uuid.uuid4()}"
collection.add(
  ids=[face_id],
  embeddings=[embedding],
  metadatas=[{"name":name}],
  documents=["Capture face"],
)  
print("Face inserted successfully!")
  

  
  




