import allure
import pytest

import data
import helpers
from api.users_api import UsersApi


@allure.feature('Пользователь: авторизация')
class TestLoginUser:

    @allure.title('Существующий пользователь может войти')
    def test_login_existing_user_returns_user_and_tokens(self, registered_user):
        response = UsersApi.login(helpers.get_credentials(registered_user))
        body = response.json()

        assert response.status_code == 200
        assert body['success'] is True
        assert body['user'] == {'email': registered_user['email'], 'name': registered_user['name']}
        assert body['accessToken'].startswith('Bearer ')
        assert body['refreshToken']

    @allure.title('Вход с неверными данными возвращает ошибку')
    @pytest.mark.parametrize('wrong_data', [
        pytest.param({'email': helpers.generate_email()}, id='неверный email'),
        pytest.param({'password': helpers.generate_random_string(10)}, id='неверный пароль'),
        pytest.param({'email': helpers.generate_email(), 'password': helpers.generate_random_string(10)},
                     id='неверны email и пароль'),
    ])
    def test_login_with_wrong_data_returns_unauthorized(self, registered_user, wrong_data):
        payload = {**helpers.get_credentials(registered_user), **wrong_data}
        response = UsersApi.login(payload)

        assert response.status_code == 401
        assert response.json() == data.LOGIN_ERROR_INCORRECT_DATA