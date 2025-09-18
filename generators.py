import random
import string


class UserGenerator:

    @staticmethod
    def generate_name():
        return f'valentin_sharonov_30_{random.randint(100, 999)}'

    @staticmethod
    def generate_email(name):
        return f'{name.lower()}@yandex.ru'

    @staticmethod
    def generate_password(length=6):
        all_chars = string.digits + string.ascii_letters
        return ''.join(random.choice(all_chars) for _ in range(length))

    @classmethod
    def generate_user(cls, valid_password=True):
        name = cls.generate_name()
        email = cls.generate_email(name)
        password = cls.generate_password(6 if valid_password else 5)
        return {
            'name': name,
            'email': email,
            'password': password
        }
