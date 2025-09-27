# USB Physical Security 🔐  

A Windows-based security solution that controls USB port access using **OTP-based authentication**, **intrusion detection via webcam**, and **centralized logging**. This project was developed as part of an internship under the guidance of **Supraja Technologies**.  

---

## 📖 Project Overview  
USB devices (pen drives, hard disks, etc.) are convenient but also pose risks such as **data theft, malware injection, and insider attacks**. Traditional solutions either permanently disable USB ports or rely on costly endpoint protection suites.  

This project proposes a **cost-effective, user-friendly, and multi-layered security system** that:  
- Requires OTP authentication before enabling/disabling USB ports.  
- Records intruder video evidence on failed attempts.  
- Logs all activities locally and remotely for accountability.  
- Provides a simple Tkinter GUI for administrators.  

---

## ⚙️ Features  
- **Email OTP Verification** – 6-digit OTP delivered via Gmail SMTP.  
- **USB Port Control** – Enable/disable USB storage dynamically via Windows Registry.  
- **Intrusion Detection** – Webcam recording when invalid OTP is entered.  
- **Logging & Reporting** – JSON logs locally + sync with server.  
- **GUI Controller** – Tkinter-based interface for admins.  

---

## 🖥️ System Architecture  
Components:  
- **GUI Controller (Tkinter)** – User interface.  
- **OTP Manager** – Generates and verifies OTPs.  
- **Email Service (SMTP)** – Sends OTPs securely.  
- **USB Controller (winreg)** – Modifies registry for port control.  
- **Intrusion Detector (OpenCV)** – Records unauthorized attempts.  
- **Logger** – Maintains structured logs and syncs to server.  

---

## 🔑 Algorithm  
1. User requests USB access → OTP generated.  
2. OTP sent to registered email.  
3. User enters OTP → System verifies.  
   - ✅ **Valid OTP** → USB enabled/disabled.  
   - ❌ **Invalid OTP** → Webcam records intruder, log entry created.  

---

## 📋 Requirements  

### Software  
- **Language:** Python 3.10+  
- **Libraries:** tkinter, smtplib, random, winreg, OpenCV (cv2), requests, dotenv  
- **OS Support:** Windows 7, 8, 10, 11 (future: Linux/Mac possible)  
- **Permissions:** Admin rights for registry edits  

### Hardware  
- Processor: Intel i3+  
- RAM: 2 GB (4 GB recommended)  
- Disk: 500 MB free  
- Webcam: Required for intrusion detection  
- Internet: Required for OTP delivery & log reporting  

---

## 🚀 Installation & Usage  

1. Clone the repo:  
   ```bash
   git clone https://github.com/<your-username>/usb-physical-security.git
   cd usb-physical-security
   ```

2. Create virtual environment:  
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Setup environment variables:  
   - Copy `.env.example` → `.env`  
   - Add your email + app password (do not commit `.env`):  
     ```env
     SMTP_SERVER=smtp.gmail.com
     SMTP_PORT=587
     SMTP_USER=your.email@example.com
     SMTP_PASS=your_app_password
     ```

4. Run as Administrator:  
   ```bash
   python src/main.py
   ```

---

## ✅ Testing  

- **Unit Tests:** OTP uniqueness, Email delivery, USB control, Webcam triggers.  
- **Integration Tests:** OTP ↔ Email, OTP ↔ USB Controller, OTP ↔ Intrusion Detector, Logger ↔ Server.  
- **System Tests:** Full workflow across Windows 7/10/11.  
- **Acceptance Tests:** Simulated real users → confirmed ease-of-use & accountability.  

---

## 📊 Results  
- Successful OTP-based USB access control.  
- Intruder recording triggered on wrong OTPs.  
- Logs captured locally & synced to server.  
- GUI tested for both technical and non-technical users.  

---

## 🔮 Future Enhancements  
- Cross-platform support (Linux, macOS).  
- AI-based intruder recognition (face detection).  
- SMS/app notifications for real-time alerts.  
- Encryption for stronger log security.  

---

## 📌 Conclusion  
This project delivers a **practical, cost-effective, and scalable** approach to USB port security. By combining **authentication (OTP)**, **monitoring (webcam)**, and **accountability (logging)**, it offers a layered defense system that can be deployed in academic labs, enterprises, and government institutions.  

---

## 🏢 Acknowledgements  
- **Internship under:** Supraja Technologies  
- **Guide:** Upendra (Senior Security Analyst)  
- **Mentorship & Support:** Supraja Technologies Cyber Security Cell  

---

## 📜 License  
This project is open-sourced under the MIT License.  
