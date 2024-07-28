import cv2
from ultralytics import YOLO
import pygame
import time
import subprocess
import os

pygame.mixer.init()
weights_path = r"C:\Users\ASUS\ProjectTesting\PythonMLProjects\MyProject\runs\detect\train\weights\best.pt"
if not os.path.exists(weights_path):
    raise FileNotFoundError(f"YOLO weights file not found at {weights_path}")
model = YOLO(weights_path)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

last_detection_time = 0
fire_detection_duration = 0
alert_delay = 5  
fire_detected = False

alert_sound_path = r"C:\Users\ASUS\ProjectTesting\PythonMLProjects\MyProject\alert.wav"
if not os.path.exists(alert_sound_path):
    raise FileNotFoundError(f"Alert sound file not found at {alert_sound_path}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    results = model.predict(source=frame)
    fire_currently_detected = False
    for result in results:
        boxes = result.boxes.xyxy.numpy()
        classes = result.boxes.cls.numpy()
        confs = result.boxes.conf.numpy()
        for i in range(len(boxes)):
            if model.names[int(classes[i])] == "Fire" and confs[i] >= 0.5:  
                x1, y1, x2, y2 = boxes[i]
                conf = confs[i]
                color = (0, 0, 255)  
                label = f"Fire {conf:.2f}"
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                fire_currently_detected = True

    if fire_currently_detected:
        if not fire_detected:
            last_detection_time = time.time()
            fire_detected = True
        else:
            fire_detection_duration = time.time() - last_detection_time
    else:
        fire_detected = False
        fire_detection_duration = 0
    if fire_detection_duration >= alert_delay:
        pygame.mixer.music.load(alert_sound_path)
        pygame.mixer.music.play()
        fire_detection_duration = 0
        try:
            subprocess.Popen(["python", r"C:\Users\ASUS\ProjectTesting\PythonMLProjects\MyProject\call.py"])
        except Exception as e:
            print(f"Failed to run call.py: {e}")

        try:
            subprocess.Popen(["python", r"C:\Users\ASUS\ProjectTesting\PythonMLProjects\MyProject\sms.py"])
        except Exception as e:
            print(f"Failed to run sms.py: {e}")

        try:
            subprocess.Popen(["python", r"C:\Users\ASUS\ProjectTesting\PythonMLProjects\MyProject\whatsapp.py"])
        except Exception as e:
            print(f"Failed to run whatsapp.py: {e}")

    
    cv2.imshow("Fire Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()