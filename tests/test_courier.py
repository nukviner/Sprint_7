import allure
import pytest
from methods.courier_methods import Courier


@allure.title('API тесты курьеров')
class TestCourier:
    @allure.title('Проверяем регистрацию курьера')
    def test_registration_courier_success(self, create_standart_courier):
        courier = create_standart_courier
        response = Courier.registration_courier(courier[0], courier[1], courier[2])
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверяем логин курьером')
    def test_logining_courier_success(self, create_random_courier):
        courier = create_random_courier
        courier_login = courier[0]
        courier_pass = courier[1]
        response = Courier.login_courier(courier_login, courier_pass)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверяем удаление курьера')
    def test_create_courier_and_delete_success(self, create_random_courier):
        courier = create_random_courier
        courier_login = courier[0]
        courier_pass = courier[1]
        response = Courier.delete_courier(Courier.get_courier_id(courier_login, courier_pass))
        assert response.status_code == 200 and response.text == '{"ok":true}'

    @allure.title('Проверяем повторную регистрацию курьера')
    def test_create_two_courier_error_create(self, create_random_courier):
        courier = create_random_courier
        courier_login = courier[0]
        courier_pass = courier[1]
        courier_name = courier[2]
        response = Courier.registration_courier(courier_login, courier_pass, courier_name)
        response_text = response.json()['message']
        assert response.status_code == 409 and response_text == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверяем регистрацию курьера с недостаточными данными')
    @pytest.mark.parametrize(
        "login, password",
        [
            ('', 'test_pass'),
            ('test_login', '')
        ]
    )
    def test_create_courier_bed_parameter_error_create(self, login, password):
        response = Courier.registration_courier(login, password, "Test_name")
        response_text = response.json()['message']
        assert response.status_code == 400 and response_text == 'Недостаточно данных для создания учетной записи'

    @allure.title('Проверяем логин курьера с некорректным паролем')
    def test_logining_courier_bad_password_error_login(self, create_random_courier):
        courier = create_random_courier
        courier_login = courier[0]
        bad_password = '123'
        response = Courier.login_courier(courier_login, bad_password)
        response_text = response.json()['message']
        assert response.status_code == 404 and response_text == 'Учетная запись не найдена'

    @allure.title('Проверяем логин курьера с некорректным логином')
    def test_logining_courier_bad_login_error_login(self, create_random_courier):
        courier = create_random_courier
        bad_login = 'not_real_courier'
        courier_password = courier[1]
        response = Courier.login_courier(bad_login, courier_password)
        response_text = response.json()['message']
        assert response.status_code == 404 and response_text == 'Учетная запись не найдена'
