import os
import time
from dotenv import load_dotenv

# Load environment variables from .env if present
load_dotenv()

def get_env_var(key, default=None):
    return os.getenv(key, default)

def current_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def mask_email(email):
    if not email or "@" not in email:
        return email
    name, domain = email.split("@")
    if len(name) > 2:
        return name[0] + "*"*(len(name)-2) + name[-1] + "@" + domain
    return "*"*len(name) + "@" + domain
