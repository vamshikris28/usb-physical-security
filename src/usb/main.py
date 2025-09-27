import tkinter as tk
from usb_physical_security.gui import USBGuardApp

if __name__ == "__main__":
    root = tk.Tk()
    app = USBGuardApp(root, receiver_email="receiver@example.com")
    root.mainloop()
