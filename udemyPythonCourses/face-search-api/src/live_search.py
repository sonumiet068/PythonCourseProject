import cv2
import numpy as np
from src.embedder import get_face_embedding
from src.search import collection

def live_search():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

    if not cap.isOpened():
        print("Camera not detected")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        emb, bbox = get_face_embedding(frame)
        if emb is not None:
            result = collection.query([emb], n_results=1)
            match_id = result["ids"][0][0]
            (x1, y1, x2, y2) = map(int, bbox)

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, f"Match: {match_id}", (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.imshow("Live Face Search", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
