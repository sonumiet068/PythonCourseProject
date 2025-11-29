import cv2
import numpy as np
from insightface.app import FaceAnalysis

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0,det_size=(640,640))

def get_embedding_from_image(image):
  faces= app.get(img=image)
  if(len(faces)==0):
    return None
  return faces[0].embedding.astype(float).tolist()

def get_faces_and_embeddings(bgr_image):
   """
    Input: BGR image (OpenCV frame)
    Returns: list of dicts: { 'bbox': (left, top, right, bottom), 'embedding': list(float) }
    If no faces: returns []
    """
   # InsightFace expects RGB numpy array
   img_rgb= bgr_image[:,:,::-1]
   faces = app.get(img_rgb)
   results =[]
   for f in faces:
     x1,y1,x2,y2 = map(int, f.bbox.astype(int))
     emb = f.embedding.astype(np.float32)
     
     #normalize embedding (very important)
     norm = np.linalg.norm(emb)
     if norm>0:
       emb = emb/norm
     results.append({
       "bbox": (x1,y1,x2,y2),
       "embedding": emb.tolist()
     })   
   return results
   
     

  
  
  
  

