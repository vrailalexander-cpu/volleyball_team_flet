import json
import os

class SettingsModel:
    FILE_PATH = "storage/settings.json"

    @classmethod
    def load_settings(cls):
        try:
            if not os.path.exists(cls.FILE_PATH):
                with open(cls.FILE_PATH, "w") as file:
                    json.dump({}, file)
            with open(cls.FILE_PATH, "r") as file:
                return json.load(file)

        except Exception as e:
            print(e)
            return {}

    @classmethod
    def save_settings(cls, data):
        try:
            with open(cls.FILE_PATH, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(e)