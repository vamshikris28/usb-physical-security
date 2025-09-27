import os
import json
import requests
from usb_physical_security.utils import current_timestamp, get_env_var

LOG_FILE = "logs.json"
LOG_SERVER_URL = get_env_var("LOG_SERVER_URL")

def log_event(event_type, details=None):
    entry = {
        "timestamp": current_timestamp(),
        "event": event_type,
        "details": details or {}
    }

    # Append to local log file
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except Exception:
            logs = []

    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"Logged event: {entry}")

    # Optionally send to server if configured
    if LOG_SERVER_URL:
        try:
            response = requests.post(LOG_SERVER_URL, json=entry, timeout=5)
            print(f"Log synced to server: {response.status_code}")
        except Exception as e:
            print(f"Failed to sync log: {e}")
