from src.models.auth_model import AuthModel

class AuthController:
    @staticmethod
    def login(name, password):
        return (
            AuthModel.validate_name(name)
            and
            AuthModel.validate_password(password)
        )