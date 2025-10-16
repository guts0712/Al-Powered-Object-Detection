🧩 𝐀𝐈-𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐎𝐛𝐣𝐞𝐜𝐭 𝐃𝐞𝐭𝐞𝐜𝐭𝐢𝐨𝐧

A real-time object detection system built with YOLOv8, OpenCV, and NumPy, capable of identifying and tracking objects in images, videos, and live webcam feeds — with automatic confidence-based logging.

🚀 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬

🎯 Detects multiple object classes (cars, people, animals, etc.) in real time

🧾 Automatically logs detections (class, confidence) above your chosen threshold

🖼️ Works on images, videos, and live webcam feeds

📊 Confidence filter for cleaner, high-accuracy results

💾 Simple file I/O integration — saves all detections into a text file

🔧 Lightweight & easy to customize

🧰 𝐓𝐞𝐜𝐡 𝐒𝐭𝐚𝐜𝐤

Language: Python 3

Libraries: Ultralytics YOLOv8, OpenCV, NumPy

⚙️ 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐚𝐭𝐢𝐨𝐧

1. Clone this repository:

git clone https://github.com/guts0712/AI-Powered-Object-Detection.git
cd AI-Powered-Object-Detection

2. Install dependencies:

pip install -r requirements.txt

3. Download YOLOv8 weights (automatically done on first run):

Default: yolov8n.pt
(You can change it to yolov8s.pt or others if needed.)

🧑‍💻 𝐔𝐬𝐚𝐠𝐞

▶️ Run on an image:

Upload an image into folder and use its path in image = cv.imread(path of your image) in image version of ai powered object detection

▶️ Run on a video:

Upload an video into folder and use its path in image = cv.videoCapture(path of your image) in video version of ai powered object detection

▶️ Run on webcam:

Just put 0 in cv.videoCapture(0)

📝 The detections (with confidence ≥ 0.6) will be saved automatically in:

detections.txt

🧾 𝐎𝐮𝐭𝐩𝐮𝐭 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:

__________________--------------NEW-VIDEO-RUN--------------__________________

Type : person --- Confidence : 0.93

__________________--------------NEW-IMAGE-RUN--------------__________________

Type : person --- Confidence : 0.91

𝐍𝐎𝐓𝐄 : This only displays or logs if the object detected is above 60% in confidence 
*also adds the detected image into a fresh folder names run 

📷 𝐒𝐜𝐫𝐞𝐞𝐧𝐬𝐡𝐨𝐭𝐬:
![image0](https://github.com/user-attachments/assets/a437f9a7-d46e-47bf-9202-83b3230f005d)

<img width="954" height="407" alt="screenshot1" src="https://github.com/user-attachments/assets/beb949f0-ef2f-4de3-89df-b397a2aa5ba6" />

<img width="951" height="382" alt="Screenshot2" src="https://github.com/user-attachments/assets/b530fc0a-a86f-4705-a4a6-66b850c3b79f" />



📁 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐒𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞

AI-Powered-Object-Detection/
│
├── main.py                 # Handles both image & video detection
├── requirements.txt        # Dependencies
├── detections.txt          # Logs (auto-generated)
├── Video folder            # For video storing and detecting
├── Image folder            # For storing images
└── README.md               # You’re reading this!

🧑‍🎓 𝐀𝐮𝐭𝐡𝐨𝐫

𝑷.𝑽 𝑨𝒎𝒐𝒈𝒉 𝑺𝒊𝒅𝒅𝒉 (𝑹𝑨2500113012225)

📬 Developed for college project & tech club submission for SRM Alexa club 

💻 Passionate about Tech




