import insightface
import numpy as np

def face_model():
  model = insightface.app.FaceAnalysis(name="buffalo_l")
  model.prepare(ctx_id=0)
  return model
