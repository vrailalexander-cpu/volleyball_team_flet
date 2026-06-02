from src.models.settings_model import SettingsModel

class SettingsController:
    @staticmethod
    def load_settings():
        return SettingsModel.load_settings()

    @staticmethod
    def save_settings(data):
        SettingsModel.save_settings(data)