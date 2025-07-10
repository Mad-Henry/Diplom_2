import allure
from methods.user_methods import UserMethods as UM
from methods.helpers import HelpersMethods as HM
from data import USER_TESTS_BEARER, USER_TESTS_ALREADY_EXISTS, USER_TESTS_REQUIRED_FILDS_ERROR, USER_TEST_AUTH_ERROR


class TestUserRegistration:


    @allure.title('Создание пользователя: создать уникального пользователя')
    def test_new_user(self, fxtr_create_and_remove_user):
        new_user_result_code, _, new_user_result_acc_tkn, _ = fxtr_create_and_remove_user
        assert new_user_result_code == 200 and USER_TESTS_BEARER in new_user_result_acc_tkn, \
            f'result_code:{new_user_result_code}, result_acc_tkn: {new_user_result_acc_tkn}'


    @allure.title('Создание пользователя: создать пользователя, который уже зарегистрирован')
    def test_new_user_dublicae(self, fxtr_create_and_remove_user):
        *_, user_dublicate_creds = fxtr_create_and_remove_user
        new_user_dblct_rslt_code, new_user_dblct_rslt_json, *_ = UM.user_register_new_one(user_dublicate_creds)
        assert new_user_dblct_rslt_code == 403 and new_user_dblct_rslt_json['message'] == USER_TESTS_ALREADY_EXISTS, \
            f'result_json: {new_user_dblct_rslt_json}'


    @allure.title('Создание пользователя: создать пользователя и не заполнить одно из обязательных полей')
    def test_new_user_not_enough_info_for_registration(self, fxtr_create_and_remove_user):
        _, new_user_not_enough_info_json, *_ = fxtr_create_and_remove_user # немного избыточное использование фикстуры.
        creds_w_email_and_name = new_user_not_enough_info_json['user']
        not_enough_info_status, not_enough_info_json, *_ =  UM.user_register_new_one(creds_w_email_and_name)
        assert not_enough_info_status == 403 and not_enough_info_json['message'] == USER_TESTS_REQUIRED_FILDS_ERROR, \
            f'result_json: {new_user_not_enough_info_json}'


class TestUserLogin:
   

    @allure.title('Логин пользователя: логин под существующим пользователем')
    def test_user_login_correct_creds(self, fxtr_create_and_remove_user):
        *_, fxtr_creds  = fxtr_create_and_remove_user
        user_email = fxtr_creds['email']
        user_pass = fxtr_creds['password']
        result_code, result_access_token = UM.user_login(user_email, user_pass)
        assert result_code == 200 and 'Bearer' in result_access_token, \
            f'code: {result_code}, token: {result_access_token}'


    @allure.title('Логин пользователя: логин с неверным логином и паролем')
    def test_user_change_profile_for_non_auth_user(self, fxtr_create_and_remove_user):
        *_, fxtr_creds  = fxtr_create_and_remove_user
        user_email = fxtr_creds['email']
        user_pass = fxtr_creds['password']
        result_code, result_access_token = UM.user_login(user_email, user_pass)
        assert result_code == 200 and 'Bearer' in result_access_token, \
            f'code: {result_code}, token: {result_access_token}'


class TestUserChangeProfile:


    @allure.title('Изменение данных пользователя:с авторизацией')
    def test_user_change_profile_for_non_auth_user(self, fxtr_create_and_remove_user):
        *_, fxtr_access_token, _  = fxtr_create_and_remove_user
        payload = HM.generate_creds()
        result_code, result_json = UM.user_change_profile(fxtr_access_token, payload)
        result_success_status = result_json['success']
        assert result_code == 200 and result_success_status == True, \
            f'code: {result_code}, result_json: {result_json}'


    @allure.title('Изменение данных пользователя: неавторизованный пользователь')
    def test_user_change_profile_for_non_auth_user(self):
        empty_access_token = ''
        payload = HM.generate_creds()
        result_code, result_json = UM.user_change_profile(empty_access_token, payload)
        result_message = result_json['message']
        assert result_code == 401 and result_message == USER_TEST_AUTH_ERROR, \
            f'code: {result_code}, result_json: {result_json}'
