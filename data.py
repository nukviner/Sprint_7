class TestData:
    standart_courier = ['someuser', 'somepass', 'somename']
    payload_order = {
        "firstName": "Имя",
        "lastName": "Фамилия",
        "address": "Адрес",
        "metroStation": 5,
        "phone": "+79991234567",
        "rentTime": 3,
        "deliveryDate": "2024-06-12",
        "comment": "Коммент",
        "color": []
    }

    colors = ['', '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']

class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    ORDER_URL = '/orders'
    GET_ORDER_ID_URL = '/orders/track'
    ACCEPT_ORDER_URL = '/orders/accept'
    COURIER_URL = '/courier'
    LOGIN_COURIER_URL = '/courier/login'
