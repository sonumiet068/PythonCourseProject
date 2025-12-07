from insightface.app import FaceAnalysis
import cv2
import numpy as np

model = None

def load_model():
    global model
    if model is None:
        model = FaceAnalysis(name='buffalo_l', root='models')
        model.prepare(ctx_id=0, det_size=(640, 640))
    return model

def get_face_embedding(image):
    app = load_model()
    faces = app.get(image)

    if len(faces) == 0:
        return None, None

    face = faces[0]             # first detected face
    return face.embedding.tolist(), face.bbox
