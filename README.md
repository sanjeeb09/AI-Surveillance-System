# 🛡️ AI Surveillance System

An AI-powered surveillance prototype that combines **Computer Vision** and **Audio Analysis** using **Sensor Fusion (Kalman Filter)** to detect suspicious activities, automatically record video clips, log events, display a monitoring dashboard, and notify users.

---

## 📌 Project Overview

This project was developed as an interview prototype to demonstrate:

- Visual Sensor Processing
- Audio Sensor Processing
- Sensor Fusion
- AI-based Suspicious Activity Detection
- Automatic Evidence Recording
- Event Logging
- Real-time Monitoring Dashboard
- Desktop Notifications

---

## 🚀 Features

- 🎥 Live Camera Monitoring
- 👤 Human Detection using YOLOv8
- 🎤 Real-time Audio Level Detection
- 🧠 Kalman Filter Sensor Fusion
- 🚨 Suspicious Activity Detection
- 📹 Automatic Video Clip Recording
- 📝 JSON Event Logging
- 📊 Streamlit Dashboard
- 🔔 Windows Desktop Notifications

---

## 🛠️ Technologies Used

- Python 3.11
- OpenCV
- YOLOv8
- Ultralytics
- NumPy
- Streamlit
- Pandas
- FilterPy (Kalman Filter)
- SoundDevice
- Plyer

---

## 📂 Project Structure

```text
AI-Surveillance-System/

app.py
dashboard.py
README.md
requirements.txt

modules/
    alerts.py
    audio.py
    camera.py
    detector.py
    event_manager.py
    fusion.py
    logger.py
    recorder.py

logs/
    events.json

clips/
    incident_demo.mp4

assets/
    camera.png
    dashboard.png
    notification.png
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI-Surveillance-System.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the AI Engine

```bash
python app.py
```

---

## ▶️ Run the Dashboard

```bash
streamlit run dashboard.py
```

---

## 📷 Screenshots

### Live Detection

*(Insert assets/camera.png here after uploading to GitHub.)*

### Dashboard

*(Insert assets/dashboard.png here after uploading to GitHub.)*

### Desktop Notification

*(Insert assets/notification.png here after uploading to GitHub.)*

---

## 🔮 Future Enhancements

- Multi-camera support
- Face recognition
- Email/SMS notifications
- Cloud storage integration
- Web-based live streaming
- Advanced anomaly detection using Deep Learning

---

## 👨‍💻 Author

**Sanjeeb Kumar Sahoo**

M.Sc. Data Science

GitHub: [Sanjeeb Sahoo](https://github.com/sanjeeb09)
