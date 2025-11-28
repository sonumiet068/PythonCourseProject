import os
import embedding_ops
import chroma_db_connections

def load_image(image_folder,collection):
  ids = []
  vectors = []
  metadatas = []
  for i,file in enumerate(os.listdir(image_folder)):
    path = os.path.join(image_folder,file)
    if(not file.lower().endswith((".jpg",".jpeg",".png"))):
      continue
    embedding= embedding_ops.get_image_embedding(path)
    ids.append(str(i))  
    vectors.append(embedding)
    metadatas.append({"filename":file,"path":path})
  collection.add(
    ids=ids,
    embeddings=vectors,
    metadatas=metadatas
  )
  print("Image inserted successfully"+ '\U0001F618')  





