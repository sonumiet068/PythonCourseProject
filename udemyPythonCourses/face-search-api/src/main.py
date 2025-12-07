from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from src.search import add_face, search_face
from src.capture import capture_image
import os

import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status":"Face search API running"}

@app.get("/capture")
def capture():
    ok, msg = capture_image()
    return {"success": ok, "path": msg}

@app.post("/insert")
def insert_face(person_id: str, file: UploadFile):
    save_path = f"captured/{person_id}.jpg"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    ok, msg = add_face(save_path, person_id)
    return {"success": ok, "message": msg}

@app.post("/search")
def find_face(file: UploadFile):
    save_path = "captured/search.jpg"
    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    result = search_face(save_path)
    print(f"Final Result>>>${result}")
    return result

@app.post("/live-search")
def live_search(payload:dict):
    action = payload.get("action")
    interval = payload.get("interval",1000)
    
    if action == "start":
        return {"status":"started","interval":interval}
    elif action == "stop":
        return {"status":"stopped"}
    else:
        return {"error":"invalid action"}

@app.get("/live-result")
def live_result():
    return latest_result or {"status":"stopped"};    