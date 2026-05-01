import json
import os

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "snake_color": [0, 255, 0],
    "grid_overlay": True,
    "sound": True
}

def load_settings():
    # create the file with default settings if it isn't there
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS
    
    try:
        with open(SETTINGS_FILE, "r") as f:
            user_settings = json.load(f)
        
        # check if any default settings are missing in user settings
        updated = False
        for key, value in DEFAULT_SETTINGS.items():
            if key not in user_settings:
                user_settings[key] = value
                updated = True
        
        if updated:
            save_settings(user_settings)
            
        return user_settings
    except (json.JSONDecodeError, Exception):
        # if the file is messed up somehow, just overwrite it with defaults
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)