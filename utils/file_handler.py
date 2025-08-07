import os
import json

LIBRARY_FILE = "data/library.json"
UPLOAD_DIR = "data/uploads"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_library(data):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_uploaded_file(uploaded_file):
    filepath = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath
