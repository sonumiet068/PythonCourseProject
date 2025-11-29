import uuid
from camera_capture import capture_from_camera
from db_setup import get_chroma_collection
from embedder import get_embedding_from_image

collection = get_chroma_collection()
name = input("Enter person name:")
count = 3
ids = []
embeddings=[]
while count>=0:
  if(count==3):
    print("Capture left face")
  elif count==2:
    print("Capture right face")
  elif count==1:
    print("Now,Capture slightly up face ")
  elif count ==0:
    print("Now,Capture slightly down face")

  img = capture_from_camera("Insert mode")
  if img is None:
    print("No image captured,Please try again!")
    continue
  emb = get_embedding_from_image(img)
  if emb is None:
    print("No face Detected,Please try again!")
    continue
  collection.add(
    ids=[f"{name}_{uuid.uuid4()}"],
    embeddings=[emb],
    metadatas=[{"name":name}],
    documents=["Capture face"],
  ) 
  count=count-1
    
print("Face inserted successfully!")
  

  
  




