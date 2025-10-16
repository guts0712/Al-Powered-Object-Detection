import cv2 as cv
from ultralytics import YOLO
import numpy as np

#Initializing 
model = YOLO('yolov8n.pt')
image =  cv.imread('Image/example.jpg')
file = open("detections.txt", "a")
file.write("\n\n__________________--------------NEW-IMAGE-RUN--------------__________________\n\n")


# fuction for rersizeing...!
def image_resize(frame, scale1 = 1.42, scale2 = 2.2):
    width = int(frame.shape[1] * scale2)
    height = int(frame.shape[0] * scale1)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Detection and display Image

results = model.predict(source = image, conf=0.5, save=True)

# For Saving into txt from torch txt via file I/O
for r in results:
    boxes = r.boxes
    for box in boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        label = model.names[class_id]
        file.write(f"Type : {label} --- Confidence : {confidence:.2f}\n")
