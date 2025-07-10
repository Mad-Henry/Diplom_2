import requests
import allure
from urls import OrderUrls as OU
from urls import BASE_URL


class OrderMethods:


    @allure.step("Получение списка заказов")
    def order_get_orders(access_token):
        access_token_hdr = {"Authorization": access_token}
        responce = requests.get(f'{BASE_URL}{OU.ORDERS_URL}', headers=access_token_hdr)
        return responce.status_code, responce.json()
    