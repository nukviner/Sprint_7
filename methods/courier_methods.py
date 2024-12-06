import requests
import random
import string
import allure
from data import Url


class Courier:

    @allure.step('Регистрация рандомного курьера')
    def register_new_courier_and_return_login_password():

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login_pass = []
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=payload)
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)
        return login_pass

    @allure.step('Регистрируем курьера')
    def registration_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=payload)
        return response

    @allure.step('Логинимся курьером')
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', data=payload)
        return response

    @allure.step('Получаем ID курьера')
    def get_courier_id(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', data=payload)
        if response.status_code == 200:
            return response.json()['id']
        else:
            return 0

    @allure.step('Удаляем курьера')
    def delete_courier(id_courier):
        response = requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/{id_courier}')
        return response
