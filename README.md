# 🍽️ Smart Food Waste Tracker & Reward System

An automated, AI-powered system designed to reduce food waste in cafeterias and mess halls. Using **Computer Vision (Google Teachable Machine)**, the system evaluates a user's plate after eating, grades their waste level, and automatically issues physical rewards via an **Arduino** or penalties via a **Caterer Database**.


## 🎯 How It Works (The Grading Logic)

The system captures an image of the plate and classifies it into one of three grades using an Image Classification Machine Learning model:

| Grade | Waste Level | System Action | Penalty / Reward |
| :---: | :--- | :--- | :--- |
| **🥇 Grade A** | **No Food Waste** | Triggers Arduino servo motor | **Dispenses a physical token** valid for one extra ladoo. |
| **🥈 Grade B** | **Little Food Waste** | System logs the event | **No action taken** (Warning threshold). |
| **🥉 Grade C** | **High Food Waste** | Captures a photo via webcam | **Uploads photo to Caterer Database** to reduce their next serving portion. |

---

## 🛠️ Tech Stack

### Software (Frontend & Backend)
*   **Python 3.x** - Main application logic and UI.
*   **Google Teachable Machine** - Image classification model training.
*   **OpenCV / TensorFlow Lite** - Real-time camera feed and ML inference.

### Hardware
*   **Arduino Uno** (or similar microcontroller) - Handles token dispenser mechanics.
*   **Servo Motor** - Physically dispenses the token on Grade A detection.
*   **Webcam / Pi Camera** - Captures plate images and user photos.

---

## 📦 Project Structure

```text
├── python_app/
│   ├── main.py              # Main Python application script
│   ├── model/               # Exported Teachable Machine model (.h5 or .tflite)
│   │   ├── keras_model.h5
│   │   └── labels.txt
│   └── database/            # Database configurations and logs
├── arduino_dispenser/
│   └── dispenser.ino        # Arduino IDE code for controlling the servo
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Hardware Assembly
1. Connect your **Servo Motor** to the Arduino board:
   * **Signal Pin** ➡️ Digital Pin 9 (or your configured pin)
   * **VCC** ➡️ 5V
   * **GND** ➡️ GND
2. Connect the Arduino to your computer via a USB cable.
3. Position your **Webcam** so it has a top-down view of the plate return area.

### 2. Arduino Setup
1. Open the `Arduino_file` file in the **Arduino IDE**.
2. Select your correct Board and COM Port.
3. Upload the code to your Arduino.

### 3. Python Software Setup
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   cd food-waste-tracker
   ```
2. Install the required Python dependencies:
   ```bash
   pip install opencv-python tensorflow numpy pyserial
   ```
3. Ensure your Arduino COM port matches the port defined in your Python script (e.g., `COM3` on Windows or `/dev/ttyUSB0` on Linux).

---

## 🚀 Running the System

1. Start the main Python program:
   ```bash
   python python_app/main.py
   ```
2. Place a finished plate under the camera.
3. The system will process the image, show the Grade output on the screen, and execute the respective hardware/database trigger automatically.

---

## 🔮 Future Enhancements
*   **Facial Recognition:** Automate student/user identification instead of manual database tagging.
*   **Analytics Dashboard:** A web interface for caterers to track monthly food waste trends.
*   **IoT Integration:** Move the database to the cloud for multi-cafeteria tracking.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
