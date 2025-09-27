import platform

def enable_usb():
    if platform.system() == "Windows":
        # TODO: Implement with winreg for Windows registry modifications
        print("USB ports enabled (stub).")
    else:
        print("USB enable not supported on this OS (yet).")

def disable_usb():
    if platform.system() == "Windows":
        # TODO: Implement with winreg for Windows registry modifications
        print("USB ports disabled (stub).")
    else:
        print("USB disable not supported on this OS (yet).")
