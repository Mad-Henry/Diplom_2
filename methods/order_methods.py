import requests
import allure
from urls import OrderUrls as OU
from urls import BASE_URL


class OrderMethods:


    @allure.step("Создание заказа")
    def order_create_order(access_token, ingridients):
        access_token_hdr = {"Authorization": access_token}
        payload = {"ingredients": ingridients}      
        responce = requests.post(f'{BASE_URL}{OU.ORDERS_URL}', data=payload, headers=access_token_hdr)
        return responce.status_code, responce.json()


    @allure.step("Получение списка заказов")
    def order_get_orders(access_token):
        access_token_hdr = {"Authorization": access_token}
        responce = requests.get(f'{BASE_URL}{OU.ORDERS_URL}', headers=access_token_hdr)
        return responce.status_code, responce.json()
    