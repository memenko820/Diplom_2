import allure
import requests

import data
import helpers


class OrdersApi:

    @staticmethod
    @allure.step('Создание заказа')
    def create(payload, token=None):
        return requests.post(f'{data.BASE_URL}{data.ORDERS_PATH}', json=payload,
                             headers=helpers.build_auth_headers(token), timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Получение заказов пользователя')
    def get_user_orders(token=None):
        return requests.get(f'{data.BASE_URL}{data.ORDERS_PATH}',
                            headers=helpers.build_auth_headers(token), timeout=data.REQUEST_TIMEOUT)