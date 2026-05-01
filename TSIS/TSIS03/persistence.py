import json
import os

SETTINGS_FILE = 'settings.json'
LEADERBOARD_FILE = 'leaderBoard.json'

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            return json.load(f)
    default = {"sound": True, "car_color": "red", "difficulty": "normal"}
    save_settings(default)
    return default

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)

def load_leaderboard():
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    return []

def save_score(name, score, distance):
    board = load_leaderboard()
    board.append({"name": name, "score": score, "distance": distance})
    board = sorted(board, key=lambda x: x['score'], reverse=True)[:10]
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(board, f, indent=4)