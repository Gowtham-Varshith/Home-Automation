Here's the final version of the README with contact information at the end:

---

# 🏡 Smart Home Automation by Gowtham Varshith

---

## 🌟 Introduction:

Welcome to the **Smart Home Automation System** developed by **Gowtham Varshith**. This project allows you to **secure**, **monitor**, and **control** your home effortlessly through your smartphone. Whether you're at home 🏠 or miles away 🌍, everything is just a tap away!

---

## 💡 Key Components:

This system is divided into two major modules:
1. **Home Security** – To safeguard your house with an intelligent security system.
2. **Home Control** – To control lights, windows, and monitor temperature, making your life smarter and easier.

---

## 🔐 Home Security Module:

### Hardware Setup:
To build this advanced security system, we used the following components:
- **Arduino Uno** for control and monitoring
- **HC-SR04 Ultrasonic Sensor** to detect visitors approaching the door
- **12V Solenoid** for automated locking of the door
- **5V Relay** to manage switching between devices
- **12V Power Supply** to keep the system powered

### Tech Stack:
- **Python** to handle the face recognition and QR code authentication
- **OpenCV** for visual processing and facial recognition
- **Firebase** for cloud-based data storage and retrieval

### Features:
- **Face Recognition**: Uses AI to identify and verify users
- **QR Code Authentication**: Offers secure entry through QR code scanning
- **Real-time Alerts**: Sends instant alerts if unauthorized access is attempted

---

## 🏠 Home Control Module:

### Hardware Components:
- **NodeMCU** for wireless control of the system
- **LEDs** for light control automation
- **SG90 Servo Motors** to automate window operations
- **DHT11 Sensors** to monitor temperature and humidity in real time

### Tech Stack:
- **React Native** for developing the user-friendly mobile app interface
- **ThingSpeak API** for connecting sensors with the web for real-time data
- **Firebase** for secure user authentication and data storage

### Key Features:
- **Remote Control**: Switch your lights on/off and control windows remotely
- **Environmental Monitoring**: Track temperature and humidity for a comfortable living environment
- **Admin Features**: Add or remove users with specific permissions

---

## 🛠️ The Journey - Challenges Faced

While building this project, there were a few challenges that needed some innovative problem-solving. Here's a little insight into the hurdles we faced and how we overcame them:

### 🚧 Challenge 1: Communication Between Python and Arduino
In the initial stages, we faced difficulties establishing smooth communication between the **Python** script and the **Arduino Uno**. The serial communication was often interrupted, and the system would stop responding.

**How We Fixed It:** After several attempts and research, we modified the baud rate and used a more robust serial library. We also introduced time delays between each command to avoid overwhelming the Arduino.

---

### 🚧 Challenge 2: Unstable Face Recognition
The face recognition algorithm sometimes failed to detect or recognize faces due to lighting conditions or poor image quality.

**How We Fixed It:** We added a pre-processing step that adjusted brightness and contrast before the image was processed by the recognition algorithm. Additionally, we improved the camera angle and used OpenCV's advanced filters for sharper image quality.

---

### 🚧 Challenge 3: Power Supply Fluctuations
During testing, we experienced inconsistent power supply issues that caused the system to reboot randomly. This affected the reliability of the project.

**How We Fixed It:** We switched to a more stable **12V power supply** with in-built voltage regulation. We also added capacitors to smooth out fluctuations, ensuring the system stayed powered consistently.

---

### 🚧 Challenge 4: Real-Time Data Delay
When we started integrating the system with **Firebase**, we noticed that the data transmission from the sensors had a slight delay, which made the control experience less seamless.

**How We Fixed It:** By optimizing the **ThingSpeak API** settings and reducing the data packet size, we managed to improve the real-time response of the system. Now, users can control their home devices with minimal delay.

---

## 🚀 Getting Started:

### Home Security Setup:

**Prerequisites:**
- Install **Python** on your machine
- Download the **Arduino IDE** for uploading the code

**Steps to Start:**
1. Clone the project:
   ```bash
   git clone https://github.com/gowthamvarshith/smart-home-automation.git
   ```
2. Set up the hardware components following the provided circuit diagram.
3. Install the Python dependencies:
   ```bash
   pip install -r security/requirements.txt
   ```
4. Upload the code to your Arduino board and run the Python script:
   ```bash
   python -m security.main
   ```

---

### Home Control Setup:

**Prerequisites:**
- Install **Node.js** for running the backend
- Set up **React Native** for the mobile application

**How to Start:**
1. Navigate to the project folder and install all necessary dependencies:
   ```bash
   npm install
   ```
2. Run the app on your Android or iOS device:
   ```bash
   npx react-native run-android
   # or
   npx react-native run-ios
   ```

---

### Firebase Setup:

1. Create a new **Firebase project**.
2. Download the **serviceAccountKey.json** and place it in the project folder.
3. Update the Firebase configuration in the app for secure data storage and retrieval.


## 📜 License:

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

### 🚀 Final Thoughts:

This project was a challenging but rewarding experience, and with this system, your home becomes smarter and more secure. Stay tuned for future updates and enhancements!

---

## 📞 Contact Info:

If you'd like to know more or have any queries, feel free to reach out!

- **Gowtham Varshith**
- Email: gowthamb461@gmail.com
- GitHub: [Gowtham Varshith](https://github.com/Gowtham-Varshith)
- Portfolio: [Gowtham's Portfolio](https://gowtham-varshith.github.io/Gowtham/)

