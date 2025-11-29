import cv2
import time
from db_setup import get_chroma_collection
from embedder import get_faces_and_embeddings,get_embedding_from_image

#Configure 
CONFIDENCE_THRESHOLD=0.80
TOP_K=1

collection = get_chroma_collection()
cap = cv2.VideoCapture(0)
if not cap.isOpened():
  print("Error:Could not open camera")
  exit
fps_time = time.time()
print("Press 'q' to quit.")

while True:
  ret,frame = cap.read()
  if not ret:
    continue
  faces = get_faces_and_embeddings(frame)
  
  for face in faces:
    x1,y1,x2,y2 = face["bbox"]
    emb = face["embedding"]  
    try:
      results = collection.query(query_embeddings=[emb],n_results=TOP_K)
    except Exception as e:
      results = {"ids":[],"distances":[],"metadatas":[[]]}
    labels = "Unknown"
    distance = "None"
    if results["distances"] and results["distances"][0]:
      distance = results["distances"][0][0]
      meta= results["metadatas"][0][0] if results["metadatas"][0][0] else {}
      if distance<CONFIDENCE_THRESHOLD:
        name = meta.get("name") or meta.get("filename") or meta.get("ids")[0][0]
        labels = f"{name} ({distance:.3f})"
      else:
        labels = f"Unknown ({distance:.3f})"
   # Draw rectangle & label
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)
    cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 200, 0), cv2.FILLED)
    cv2.putText(frame, labels, (x1 + 3, y2 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1) 
       
  fps = 1.0/ (time.time()-fps_time) if time.time()-fps_time>0 else 0.0
  fps_time = time.time()
  cv2.putText(frame,f"FPS: {fps:.1f}",(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
  cv2.imshow("Live Face Search (InsightFace + ChromaDB)", frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()       
      
      


