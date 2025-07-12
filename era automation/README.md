# 🚀 ERA Explorer Automation Project

A complete automation system built for ERA Explorer that smartly handles application flow—from launching and navigating the UI to session detection and completion—with **zero mouse or keyboard input** by the user.

---

## 🧠 Project Overview

This project contains **two core automation approaches**:

### 1. ✅ PyWinAuto-Based GUI Automation (`DiffTechnologies.py`)
- Uses `pywinauto` with UIA backend to launch ERA Explorer.
- Waits for the “Proceed” button using native GUI controls.
- Detects and clicks **Skip Wizard** using smart window detection—**no coordinates needed**.

### 2. 🔁 Full Session Automation (`EraStart.py`)
- Fully automates user login from a CSV.
- Waits for system readiness via OCR.
- Navigates the ERA Explorer UI.
- Detects **incomplete sessions** (without green lines).
- Completes 2 sessions per user, including videos and tasks.
- Logs out and moves to the next user.

---

## ⚙️ System Requirements

- **OS:** Windows 10 or above
- **Python:** 3.8+
- **Admin rights:** Required
- **ERA Explorer Installed at:**  
  `C:\Program Files\ERA Explorer\ERA Explorer.exe`

---

## 📦 Dependencies

Install using:

```bash
pip install -r requirements.txt
```

### Required Libraries
- `pywinauto`
- `pyautogui`
- `opencv-python`
- `pytesseract`
- `pandas`
- `keyboard`
- `Pillow`

Also install **Tesseract-OCR** separately and ensure it's in system path.

---

## 📁 Project Structure

```
ERA_Automation_Project/
│
├── pywinauto_automation.py     # Smart UI Automation (No Coordinates)
├── full_automation.py          # Full login + session automation
├── credentials.csv             # Login credentials (sample format)
├── requirements.txt            # Python dependencies
├── assets/                     # Screenshots / images for OCR detection
└── README.md                   # Project documentation (this file)
```

---

## ▶️ Running the Code

### Run UI-based automation:
```bash
python pywinauto_automation.py
```

### Run full automation:
```bash
python full_automation.py
```

Make sure your credential CSV and image assets are correctly placed and paths updated.

---

## 🧪 Compatibility & Stability

- ✅ Works on different screen sizes with OCR + image template matching.
- ✅ No hard-coded coordinates (in PyWinAuto version).
- ✅ Tested on multiple systems running ERA Explorer.

---

## 👨‍💻 Author

**Tabish Deshmukh**  
Assistant Director, Deshmukh Computer  
🛠 Building smart automation systems for real-world government apps  
🔗 [YouTube Channel](https://youtube.com/@humteendost?si=mBw8ymoqNNhyGOT0)

---

## 📌 Notes

- Ensure no interfering popups block ERA Explorer.
- Maintain stable internet for ERA to fetch session data.
- You may update OCR/image paths as per screen resolution for better precision.

---

---

### 📌 Coordinate-Based Automation Script (Legacy Method)

In earlier stages, the automation system was built using screen coordinate-based clicking (via `pyautogui`). This method involved locating specific UI elements using hard-coded (x, y) pixel values such as the "Proceed", "Skip Wizard", "Login", and "Resume Learning" buttons. It was functional but rigid—any change in screen resolution or layout would break it.

#### ✅ Use Cases:
- Systems without UI automation support.
- Rapid prototyping when element names/controls are not available.

#### ❌ Limitations:
- Not resolution-independent.
- Fails on UI changes or slow app loads.

The new Pywinauto and Image-based hybrid method fully replaces this approach with more flexibility and smart detection.
