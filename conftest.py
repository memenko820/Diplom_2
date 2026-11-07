import pytest

import helpers
from api.ingredients_api import IngredientsApi
from api.orders_api import OrdersApi
from api.users_api import UsersApi


@pytest.fixture
def new_user_payload():
    # Данные для регистрации
    payload = helpers.generate_user_payload()

    yield payload

    UsersApi.delete_by_credentials(payload['email'], payload['password'])


@pytest.fixture
def registered_user():
    # Пользователь, зарегистрированный до теста: данные и токен авторизации
    payload = helpers.generate_user_payload()
    response = UsersApi.register(payload)
    user = {**payload, 'token': response.json()['accessToken']}

    yield user

    UsersApi.delete(user['token'])


@pytest.fixture
def ingredient_ids():
    # Два ингредиента из списка, который отдаёт сервис
    ingredients = IngredientsApi.get_ingredients().json()['data']

    return [ingredients[0]['_id'], ingredients[1]['_id']]


@pytest.fixture
def user_with_order(registered_user, ingredient_ids):
    # Зарегистрированный пользователь с одним созданным заказом
    response = OrdersApi.create({'ingredients': ingredient_ids}, registered_user['token'])

    return {**registered_user, 'order_number': response.json()['order']['number']}