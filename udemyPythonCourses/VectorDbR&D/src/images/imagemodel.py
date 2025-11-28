import torch
from torchvision import transforms
from transformers import CLIPModel,CLIPProcessor

model_name = "openai/clip-vit-base-patch32"

def get_image_model():
  model = CLIPModel.from_pretrained(model_name)
  return model
  
def get_image_process():  
  processor = CLIPProcessor.from_pretrained(model_name,use_fast=True)
  return processor



 
 
 