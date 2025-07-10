import allure
import string
import random


class HelpersMethods:


    @staticmethod
    @allure.step('Генерация строки')
    def generate_string(length):
        letters = string.ascii_lowercase
        gen_str = ''.join(random.choice(letters) for i in range(length))
        return gen_str


    @staticmethod
    @allure.step('Генерация кредов (email, password, name)')
    def generate_creds():
        gen_email = f'"mad-henry-{HelpersMethods.generate_string(3)}@yandex.ru"'
        gen_password = f'"Mad-Henry-{HelpersMethods.generate_string(3)}-777"'
        gen_name = f'"mad-henry-{HelpersMethods.generate_string(5)}"'
        creds = {
            "email": f'{gen_email}',
            "password": f'{gen_password}',
            "name": f'{gen_name}'
                    }
        return creds
