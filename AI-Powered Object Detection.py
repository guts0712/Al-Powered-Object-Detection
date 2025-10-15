import cv2 as cv
from ultralytics import YOLO
import numpy as np

model = YOLO('yolov8n.pt')

video = cv.VideoCapture(0) 

def video_resize(frame, scale1 = 1.42, scale2 = 2.2):
    width =  int(frame.shape[1] * scale2)
    height = int(frame.shape[0] * scale1)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

if not video.isOpened():
    print("Error: Could not open video stream or file.")
    exit()

print("Starting real time detection. Press 'q' to exit.")

while video.isOpened():

    success, frame = video.read()
    
    if success:
        flipped_frame = cv.flip(frame, 1)
        results = model.predict(source=flipped_frame, stream=False, verbose=False) 
        annotated_frame = results[0].plot()

        cv.imshow("AL-Powered Object Detection", video_resize(annotated_frame))

        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

video.release()
cv.destroyAllWindows()