import tkinter as tk
from tkinter import messagebox, simpledialog

from usb_physical_security.otp_manager import generate_otp, send_otp_email
from usb_physical_security.usb_controller import enable_usb, disable_usb
from usb_physical_security.intrusion_detector import record_intrusion
from usb_physical_security.logger import log_event

class USBGuardApp:
    def __init__(self, root, receiver_email="receiver@example.com"):
        self.root = root
        self.root.title("USB Physical Security")
        self.root.geometry("400x300")
        self.otp = None
        self.receiver_email = receiver_email

        tk.Label(root, text="USB Physical Security", font=("Arial", 16, "bold")).pack(pady=10)

        self.info_label = tk.Label(root, text="Click to generate OTP")
        self.info_label.pack(pady=5)

        tk.Button(root, text="Generate OTP", command=self.handle_generate_otp).pack(pady=5)
        tk.Button(root, text="Enable USB", command=self.handle_enable_usb).pack(pady=5)
        tk.Button(root, text="Disable USB", command=self.handle_disable_usb).pack(pady=5)

    def handle_generate_otp(self):
        self.otp = generate_otp()
        try:
            send_otp_email(self.receiver_email, self.otp)
            self.info_label.config(text="OTP sent to email")
            log_event("OTP_GENERATED", {"receiver": self.receiver_email})
        except Exception as e:
            self.info_label.config(text=f"OTP send failed: {e}")
            log_event("OTP_SEND_FAILED", {"error": str(e)})
        print(f"[DEBUG] OTP (for testing): {self.otp}")

    def handle_enable_usb(self):
        if self.prompt_for_otp():
            enable_usb()
            log_event("USB_ENABLED")

    def handle_disable_usb(self):
        if self.prompt_for_otp():
            disable_usb()
            log_event("USB_DISABLED")

    def prompt_for_otp(self):
        if not self.otp:
            messagebox.showerror("Error", "No OTP generated yet.")
            return False
        user_otp = simpledialog.askstring("OTP Verification", "Enter OTP:")
        if user_otp == self.otp:
            messagebox.showinfo("Success", "OTP Verified")
            log_event("OTP_VERIFIED")
            return True
        else:
            messagebox.showerror("Failed", "Invalid OTP! Intrusion logged.")
            intrusion_file = record_intrusion()
            log_event("INTRUSION_ATTEMPT", {"intrusion_file": intrusion_file})
            return False
