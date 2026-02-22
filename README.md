# Gesture Based Volume Control

## 📌 Description
This project implements a real-time hand gesture based system volume controller.
Using a webcam and MediaPipe hand landmark detection, the system detects the
distance between the thumb and index finger and adjusts system volume accordingly.

## ✋ Gesture Used
- **Pinch Gesture (Thumb + Index Finger)**  
  - Increase distance → Increase volume  
  - Decrease distance → Decrease volume  

## 🛠 Technologies Used
- Python
- OpenCV
- MediaPipe
- Streamlit
- Pycaw (Windows Audio Control)

## ▶ How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python run_app.py

## 🎯 Output
Real-time webcam feed with gesture-based system volume control.
