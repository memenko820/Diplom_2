import allure
import pytest

import data
import helpers
from api.orders_api import OrdersApi


@allure.feature('Заказы: создание заказа')
class TestCreateOrder:

    @allure.title('Авторизованный пользователь может создать заказ')
    def test_create_order_with_auth_returns_order_number(self, registered_user, ingredient_ids):
        response = OrdersApi.create({'ingredients': ingredient_ids}, registered_user['token'])
        body = response.json()

        assert response.status_code == 200
        assert body['success'] is True
        assert body['name']
        assert isinstance(body['order']['number'], int)

    @allure.title('Неавторизованный пользователь может создать заказ')
    def test_create_order_without_auth_returns_order_number(self, ingredient_ids):
        response = OrdersApi.create({'ingredients': ingredient_ids})
        body = response.json()

        assert response.status_code == 200
        assert body['success'] is True
        assert body['name']
        assert isinstance(body['order']['number'], int)

    @allure.title('В заказ попадают переданные ингредиенты')
    def test_create_order_with_ingredients_returns_same_ingredients(self, registered_user, ingredient_ids):
        response = OrdersApi.create({'ingredients': ingredient_ids}, registered_user['token'])
        body = response.json()

        assert response.status_code == 200
        assert helpers.extract_values(body['order']['ingredients'], '_id') == ingredient_ids

    @allure.title('Нельзя создать заказ без ингредиентов')
    @pytest.mark.parametrize('payload', [
        pytest.param({'ingredients': []}, id='пустой список'),
        pytest.param({}, id='нет поля ingredients'),
    ])
    def test_create_order_without_ingredients_returns_bad_request(self, registered_user, payload):
        response = OrdersApi.create(payload, registered_user['token'])

        assert response.status_code == 400
        assert response.json() == data.ORDER_ERROR_NO_INGREDIENTS

    @allure.title('Заказ с неверным хешем ингредиента возвращает ошибку сервера')
    def test_create_order_with_invalid_hash_returns_server_error(self, registered_user):
        response = OrdersApi.create({'ingredients': [data.INVALID_INGREDIENT_HASH]}, registered_user['token'])

        assert response.status_code == 500
        assert data.ORDER_ERROR_INVALID_HASH_TEXT in response.text