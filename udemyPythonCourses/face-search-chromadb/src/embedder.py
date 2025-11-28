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
  

