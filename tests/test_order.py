import allure
from methods.order_methods import OrderMethods as OM


class TestOrders:


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
