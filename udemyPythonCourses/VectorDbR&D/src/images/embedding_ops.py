import numpy as np
from PIL import Image
import imagemodel
import torch
from torchvision import transforms
from transformers import CLIPModel,CLIPProcessor

model = imagemodel.get_image_model()
processor = imagemodel.get_image_process()
# --------- Helper: Convert image → vector --------- #
def get_image_embedding(image_path):
  image = Image.open(image_path).convert("RGB")
  inputs = processor(images=image,return_tensors="pt")
  with torch.no_grad():
      vector = model.get_image_features(**inputs)
  vector = vector/vector.norm() #normalize
  return vector.squeeze().tolist() 

# --------------- GET Text Embedding ---------------------------
def get_text_embedding(text_query):
  inputs = processor(text=[text_query],return_tensors="pt",padding=True)
  with torch.no_grad():
       vector = model.get_text_features(**inputs)
  vector = vector/vector.norm() #normalize
  return vector.squeeze().tolist()  #convert tensor -> list
   
