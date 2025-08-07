import os
import json

LIBRARY_FILE = "data/library.json"
UPLOAD_DIR = "data/uploads"

def load_library():
    if not os.path.exists("library.json"):
        return {}
    with open("library.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_library(data):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(data, f, indent=4)

import os

def save_uploaded_file(uploaded_file):
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)  # ✅ Create folder if missing

    filepath = os.path.join(upload_dir, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath

