import cv2 as cv
from ultralytics import YOLO
import numpy as np

#Initializing 
model = YOLO('yolov8n.pt')
video = cv.VideoCapture(0)
file = open("detections.txt", "a")
file.write("\n\n__________________--------------NEW-VIDEO-RUN--------------__________________\n\n")

#function for rersizeing...!
def video_resize(frame, scale1 = 1.42, scale2 = 2.2):
    width = int(frame.shape[1] * scale2)
    height = int(frame.shape[0] * scale1)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#Opening Webcam
if not video.isOpened():
    print("Error: Could not open video stream or file.")
    exit()

print("Starting real time detection. Press 'q' to exit.")

#Detection and display Video
while video.isOpened():
    success, frame = video.read()

    if success:
        flipped_frame = cv.flip(frame, 1)
        results = model.predict(source=flipped_frame, stream=False, verbose=False) 
        annotated_frame = results[0].plot()
        cv.imshow("AI-Powered Video Object Detection", video_resize(annotated_frame))
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

#For Saving into txt from torch txt via file I/O
for r in results:
    boxes = r.boxes
    for box in boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = model.names[class_id]
        if confidence > 0.6:
            file.write(f"Type : {label} --- Confidence : {confidence:.2f}\n")

video.release()
cv.destroyAllWindows()