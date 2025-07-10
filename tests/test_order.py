import allure
from methods.order_methods import OrderMethods as OM
from data import ORDER_ONE_INGRIDIENT, ORDER_TWO_INGRIDIENTS, ORDER_EMPTY_INGRIDIENTS, ORDER_EMPTY_INGRIDIENTS_ERROR, ORDER_WRONG_HASH_INGRIDIENT, ORDER_WRONG_HASH_INGRIDIENT_ERROR


class TestOrderCreation:


    @allure.title('Создание заказа: с авторизацией')
    def test_order_create_with_auth_user(self, fxtr_create_and_remove_user):
        *_, fxtr_acces_token, _ = fxtr_create_and_remove_user
        order_creation_status, order_creation_message = OM.order_create_order(fxtr_acces_token, ORDER_ONE_INGRIDIENT)
        order_creation_order_dict = order_creation_message['order']
        assert order_creation_status == 200 and 'owner' in order_creation_order_dict, \
            f'Status: {order_creation_status}, Order dict: {order_creation_order_dict}'



    @allure.title('Создание заказа: без авторизации')
    def test_order_create_with_non_auth_user(self):
        acces_token = ''
        order_creation_status, order_creation_message = OM.order_create_order(acces_token, ORDER_ONE_INGRIDIENT)
        order_creation_order_dict = order_creation_message['order']
        assert order_creation_status == 200 and 'owner' not in order_creation_order_dict, \
            f'Status: {order_creation_status}, Order dict: {order_creation_order_dict}'


    @allure.title('Создание заказа: с ингредиентами')
    def test_order_create_with_ingridients(self, fxtr_create_and_remove_user):
        *_, fxtr_acces_token, _ = fxtr_create_and_remove_user
        order_creation_status, order_creation_message = OM.order_create_order(fxtr_acces_token, ORDER_TWO_INGRIDIENTS)
        order_creation_order_dict = order_creation_message['order']
        assert order_creation_status == 200 and 'owner' in order_creation_order_dict, \
            f'Status: {order_creation_status}, Order dict: {order_creation_order_dict}'


    @allure.title('Создание заказа: без ингредиентов')
    def test_order_create_without_ingridients(self, fxtr_create_and_remove_user):
        *_, fxtr_acces_token, _ = fxtr_create_and_remove_user
        order_creation_status, order_creation_message = OM.order_create_order(fxtr_acces_token, ORDER_EMPTY_INGRIDIENTS)
        order_creation_message = order_creation_message['message']
        assert order_creation_status == 400 and order_creation_message == ORDER_EMPTY_INGRIDIENTS_ERROR , \
            f'Status: {order_creation_status}, Message: {order_creation_message}'


    @allure.title('Создание заказа: с неверным хешем ингредиентов')
    def test_order_create_with_wrongs_ingridients(self, fxtr_create_and_remove_user):
        *_, fxtr_acces_token, _ = fxtr_create_and_remove_user
        order_creation_status, order_creation_message = OM.order_create_order(fxtr_acces_token, ORDER_WRONG_HASH_INGRIDIENT)
        order_creation_message = order_creation_message['message']
        assert order_creation_status == 400 and order_creation_message == ORDER_WRONG_HASH_INGRIDIENT_ERROR , \
            f'Status: {order_creation_status}, Message: {order_creation_message}'


class TestOrderGetting:


    @allure.title('Получение заказов конкретного пользователя: авторизованный пользователь')
    def test_order_get_order_for_auth_user(self, fxtr_create_and_remove_user):
        _, _, xftr_access_token, _ = fxtr_create_and_remove_user
        orders_status, orders_message = OM.order_get_orders(xftr_access_token)
        orders_message_success = orders_message['success']
        assert orders_status == 200 and orders_message_success is True, \
            f'status: {orders_status}, success state: {orders_message_success}'
        

    @allure.title('Получение заказов конкретного пользователя: неавторизованный пользователь')
    def test_order_get_order_for_non_auth_user(self):
        empty_token = ''
        orders_status, orders_message = OM.order_get_orders(empty_token)
        orders_message_success = orders_message['success']
        assert orders_status == 401 and orders_message_success is False, \
            f'status: {orders_status}, success state: {orders_message_success}'
