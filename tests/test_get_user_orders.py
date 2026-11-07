import allure

import data
import helpers
from api.orders_api import OrdersApi


@allure.feature('Заказы: заказы пользователя')
class TestGetUserOrders:

    @allure.title('Авторизованный пользователь видит свои заказы')
    def test_get_orders_with_auth_returns_user_orders(self, user_with_order):
        response = OrdersApi.get_user_orders(user_with_order['token'])
        body = response.json()

        assert response.status_code == 200
        assert body['success'] is True
        assert helpers.extract_values(body['orders'], 'number') == [user_with_order['order_number']]

    @allure.title('Неавторизованный пользователь не получает заказы')
    def test_get_orders_without_auth_returns_unauthorized(self):
        response = OrdersApi.get_user_orders()

        assert response.status_code == 401
        assert response.json() == data.ERROR_UNAUTHORIZED