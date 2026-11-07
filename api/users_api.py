import allure
import requests

import data
import helpers


class UsersApi:

    @staticmethod
    @allure.step('Регистрация пользователя')
    def register(payload):
        return requests.post(f'{data.BASE_URL}{data.REGISTER_PATH}', json=payload, timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Логин пользователя')
    def login(payload):
        return requests.post(f'{data.BASE_URL}{data.LOGIN_PATH}', json=payload, timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Изменение данных пользователя')
    def update(payload, token=None):
        return requests.patch(f'{data.BASE_URL}{data.USER_PATH}', json=payload,
                              headers=helpers.build_auth_headers(token), timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete(token):
        return requests.delete(f'{data.BASE_URL}{data.USER_PATH}',
                               headers=helpers.build_auth_headers(token), timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Удаление пользователя по email и паролю')
    def delete_by_credentials(email, password):
        """Удаляет пользователя, если он существует в системе."""
        login_response = UsersApi.login({'email': email, 'password': password})

        if login_response.status_code == 200:
            UsersApi.delete(login_response.json()['accessToken'])