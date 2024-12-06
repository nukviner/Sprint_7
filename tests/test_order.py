import allure
import pytest
import data
import json
from methods.order_methods import Order
from methods.courier_methods import Courier


@allure.title('API тесты заказов')
class TestOrder:
    @allure.title('Проверяем создание заказа')
    def test_create_order_success(self):
        response = Order.create_order(data.TestData.payload_order)
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверяем подтверждение заказа')
    def test_accept_order_success(self, create_random_courier):
        courier = create_random_courier
        courier_id = Courier.login_courier(courier[0], courier[1]).json()['id']
        order_track = Order.create_order(data.TestData.payload_order).json()["track"]
        order_id = Order.get_id_order(order_track)

        response = Order.accept_order(courier_id, order_id)
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверяем получение списка заказов')
    def test_get_list_orders_success(self, create_random_courier):
        courier = create_random_courier
        courier_id = Courier.login_courier(courier[0], courier[1]).json()['id']
        order_track = Order.create_order(data.TestData.payload_order).json()["track"]
        order_id = Order.get_id_order(order_track)
        Order.accept_order(courier_id, order_id)

        response = Order.get_list_orders(courier_id)

        assert (response.status_code == 200 and courier_id == response.json()['orders'][0]['courierId'] and
                order_track == response.json()['orders'][0]['track'])

    @allure.title('Проверяем создание заказа с различными вариантами цветов')
    @pytest.mark.parametrize('color', data.TestData.colors)
    def test_crate_order_diff_colors_success(self, color):
        order_data = data.TestData.payload_order['color'] = color
        json_data = json.dumps(order_data)
        response = Order.create_order(json_data)
        assert response.status_code == 201 and 'track' in response.text
