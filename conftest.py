import pytest
import data
from methods.courier_methods import Courier


@pytest.fixture
def create_random_courier():
    courier = Courier.register_new_courier_and_return_login_password()
    yield courier
    Courier.delete_courier(Courier.get_courier_id(courier[0], courier[1]))

@pytest.fixture
def create_standart_courier():
    courier = data.TestData.standart_courier
    yield courier
    Courier.delete_courier(Courier.get_courier_id(courier[0], courier[1]))
