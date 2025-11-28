import cv2

def capture_from_camera(window_name="Camera"):
  cam = cv2.VideoCapture(0)
  print("Press space to capture photo or Q to quit")
  
  while True:
    ret,frame = cam.read()
    if not ret:
      continue
    cv2.imshow(window_name,frame)
    key = cv2.waitKey(1)
    
    if key==32:
      img = frame.copy()
      cam.release()
      cv2.destroyAllWindows()
      return img
    
    if key==ord("q"):
      cam.release()
      cv2.destroyAllWindows()
      return None
    
    
    
    
  