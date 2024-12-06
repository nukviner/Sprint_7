import requests
import allure
from data import Url

class Order:
    @allure.step('Создаем заказ')
    def create_order(order):
        response = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', data=order)
        return response

    @allure.step('Получаем ID заказа')
    def get_id_order(track_order):
        payload = {"t": track_order}
        response = requests.get(f'{Url.BASE_URL}{Url.GET_ORDER_ID_URL}', params=payload)
        return response.json()['order']['id']

    @allure.step('Подтверждаем заказ')
    def accept_order(courier_id, order_id):
        payload = {"courierId": (courier_id)}
        response = requests.put(f'{Url.BASE_URL}{Url.ACCEPT_ORDER_URL}/{order_id}', params=payload)
        return response

    @allure.step('Получаем список заказов')
    def get_list_orders(courier_id):
        payload = {"courierId": (courier_id)}
        response = requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}', params=payload)
        return response
