import json
import os
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "events.json")


def _ensure_log_file():
    """Create the logs directory and JSON file if they don't exist."""

    os.makedirs(LOG_DIR, exist_ok=True)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)


def log_event(people, confidence, audio, fusion_score, status, clip):
    """
    Save a suspicious activity event to events.json.
    """

    _ensure_log_file()

    event = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "people": int(people),
        "confidence": round(float(confidence), 2),
        "audio": round(float(audio), 2),
        "fusion": round(float(fusion_score), 2),
        "status": status,
        "clip": clip if clip else "N/A"
    }

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            events = json.load(file)

            if not isinstance(events, list):
                events = []

    except (json.JSONDecodeError, FileNotFoundError):
        events = []

    events.append(event)

    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    print(
        f"📝 Event logged | "
        f"People: {people} | "
        f"Audio: {audio:.2f} | "
        f"Fusion: {fusion_score:.2f}"
    )


def get_events():
    """Return all previously logged events."""

    _ensure_log_file()

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            events = json.load(file)

            if isinstance(events, list):
                return events

    except (json.JSONDecodeError, FileNotFoundError):
        pass

    return []