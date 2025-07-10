import requests
import allure
from methods.helpers import HelpersMethods as HM
from urls import BASE_URL, USER_REGISTRATION_URL, USER_LOGIN_URL, USER_PROFILE_UPDATE_URL


class UserMethods:


    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def user_register_new_one(creds=None):
        if creds is None:
            creds = HM.generate_creds()
        payload = creds
        responce = requests.post(f'{BASE_URL}{USER_REGISTRATION_URL}', data=payload)
        return responce.status_code, responce.json(), creds


    @allure.step("Логин пользователя")
    def user_login(login, password):
        payload={
            "email":login,
            "password":password
            }
        responce = requests.post(f'{BASE_URL}{USER_LOGIN_URL}', data=payload)
        access_token = responce.json()['accessToken']
        return responce.status_code, access_token


    @allure.step("Изменение данных пользователя")
    def user_change_profile(access_token, payload):
        access_token_hdr = {"Authorization": access_token}
        responce = requests.patch(f'{BASE_URL}{USER_PROFILE_UPDATE_URL}', data=payload, headers=access_token_hdr)
        return responce.status_code, responce.json()

    """
    @allure.step("Логаут пользователя")
    def user_logout(refresh_token):
        payload={"token": "{f'{refresh_token}'}"}
        responce = requests.post(f'{BASE_URL}{USER_LOGOUT_URL}', data=payload)
        #return responce.status_code #!?!?!??!
        pass
    """

    @staticmethod
    @allure.step("Удаление пользователя")
    def user_delete_profile(access_token):
        access_token_hdr = {"Authorization": access_token}
        responce = requests.delete(f'{BASE_URL}{USER_PROFILE_UPDATE_URL}', headers=access_token_hdr)
        return responce.status_code, responce.json()