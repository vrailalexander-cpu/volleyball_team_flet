import re

class AuthModel:
    @staticmethod
    def validate_name(name):
        pattern = r"^[A-Za-zА-Яа-яІіЇїЄє]{3,20}$"
        return re.match(pattern, name)

    @staticmethod
    def validate_password(password):
        pattern = r"^[A-Za-z0-9_@#$]{6,20}$"
        return re.match(pattern, password)