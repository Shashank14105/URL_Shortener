import json
import os
import threading

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "urls.json")

# A lock so concurrent requests don't corrupt the JSON file
_lock = threading.Lock()


def _ensure_data_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)


def load_all() -> dict:
    
    _ensure_data_file()
    with _lock:
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}


def save_all(data: dict):
    
    _ensure_data_file()
    with _lock:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)


def add_url(short_code: str, original_url: str):
    
    data = load_all()
    data[short_code] = {"original_url": original_url, "clicks": 0}
    save_all(data)


def get_url(short_code: str):
    
    data = load_all()
    return data.get(short_code)


def increment_clicks(short_code: str):
    
    data = load_all()
    if short_code in data:
        data[short_code]["clicks"] += 1
        save_all(data)


def code_exists(short_code: str) -> bool:
    data = load_all()
    return short_code in data
