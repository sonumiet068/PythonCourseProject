import cv2
import uuid
import os


def capture_image(save_path="captured/captured.jpg"):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return False, "Could not open camera"

    ret, frame = cap.read()
    if not ret:
        return False, "Failed to capture frame"

    os.makedirs("captured", exist_ok=True)
    cv2.imwrite(save_path, frame)
    cap.release()
    return True, save_path
