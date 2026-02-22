# 🎛️ Gesture Volume Control with Hand Gestures

## 📌 Project Overview
This project implements a **real-time gesture-based system volume controller** using computer vision.
A webcam captures hand movements, and the distance between the **thumb and index finger** is used to
dynamically control the system volume without touching the keyboard or mouse.

The application provides a **hands-free, intuitive, and interactive user experience**, making it useful
for smart systems, accessibility applications, and human–computer interaction research.

---

## 🎯 Objectives
- To detect human hand gestures in real time using a webcam  
- To control system volume using natural hand movements  
- To build an interactive and user-friendly interface using Streamlit  
- To demonstrate practical use of computer vision in real-world applications  

---

## ✋ Gestures Implemented
### 1️⃣ Pinch Gesture (Thumb + Index Finger)
- Increasing the distance between fingers → **Increase Volume**
- Decreasing the distance between fingers → **Decrease Volume**

The gesture is continuously tracked, allowing smooth and responsive volume control.

---

## 🛠️ Technologies & Tools Used
- **Python** – Core programming language  
- **OpenCV** – Webcam access and image processing  
- **MediaPipe** – Hand landmark detection  
- **PyCaw** – System audio control (Windows)  
- **Streamlit** – Web-based user interface  

---

## 🧩 System Architecture
1. Webcam captures real-time video frames  
2. MediaPipe detects hand landmarks  
3. Distance between thumb and index finger is calculated  
4. Distance is mapped to system volume range  
5. PyCaw updates system volume accordingly  
6. Streamlit displays live video and volume status  

---

## 📂 Project Structure
Gesture-Volume-Control-with-Hand-Gestures/
│
├── app.py # Main Streamlit application
├── handgesture.py # Hand gesture detection & volume logic
├── run_app.py # Application launcher
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── LICENSE # License file
└── .gitignore # Ignored files


---
## ▶️ How to Run the Project

### Step 1: Install Dependencies
  '''bash
  pip install -r requirements.txt 

### Step 2: Run the Application
  python run_app.py

### Step 3: Use the Application
  Allow webcam access
  Show your hand to the camera
  Use pinch gesture to control volume
  Click Stop Camera to end


---
### 🖥️ Output

Live webcam feed displayed in browser

Real-time hand landmark visualization

Smooth volume adjustment based on gesture

Volume percentage displayed on UI


---
⚠️ Limitations

Works only on Windows OS (PyCaw dependency)

Requires good lighting for accurate hand detection

Single-hand gesture support


---
🎓 Conclusion

This project demonstrates how computer vision and gesture recognition can be combined to create
natural and touchless interfaces. It highlights the practical use of MediaPipe and OpenCV in real-time
applications and serves as a strong foundation for advanced gesture-controlled systems.


---
👤 Author

Aasif N


---
📜 License

This project is licensed under the MIT License.
