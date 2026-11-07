import allure
import pytest

import data
import helpers
from api.users_api import UsersApi


@allure.feature('Пользователь: регистрация')
class TestCreateUser:

    @allure.title('Можно создать уникального пользователя')
    def test_register_unique_user_returns_user_and_tokens(self, new_user_payload):
        response = UsersApi.register(new_user_payload)
        body = response.json()

        assert response.status_code == 200
        assert body['success'] is True
        assert body['user'] == {'email': new_user_payload['email'], 'name': new_user_payload['name']}
        assert body['accessToken'].startswith('Bearer ')
        assert body['refreshToken']

    @allure.title('Нельзя создать уже зарегистрированного пользователя')
    def test_register_existing_user_returns_forbidden(self, registered_user):
        payload = helpers.remove_field(registered_user, 'token')
        response = UsersApi.register(payload)

        assert response.status_code == 403
        assert response.json() == data.REGISTER_ERROR_USER_EXISTS

    @allure.title('Нельзя создать пользователя без обязательного поля')
    @pytest.mark.parametrize('missing_field', [
        pytest.param('email', id='без email'),
        pytest.param('password', id='без пароля'),
        pytest.param('name', id='без имени'),
    ])
    def test_register_without_required_field_returns_forbidden(self, new_user_payload, missing_field):
        payload = helpers.remove_field(new_user_payload, missing_field)
        response = UsersApi.register(payload)

        assert response.status_code == 403
        assert response.json() == data.REGISTER_ERROR_REQUIRED_FIELDS