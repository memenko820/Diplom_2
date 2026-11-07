import allure
import pytest

import data
import helpers
from api.users_api import UsersApi


@allure.feature('Пользователь: изменение данных')
class TestUpdateUser:

    @allure.title('Авторизованный пользователь может изменить поле')
    @pytest.mark.parametrize('changes', [
        pytest.param({'email': helpers.generate_email()}, id='email'),
        pytest.param({'name': helpers.generate_random_string(10)}, id='имя'),
    ])
    def test_update_field_with_auth_returns_updated_user(self, registered_user, changes):
        response = UsersApi.update(changes, registered_user['token'])
        expected_user = {'email': registered_user['email'], 'name': registered_user['name'], **changes}

        assert response.status_code == 200
        assert response.json() == {'success': True, 'user': expected_user}

    @allure.title('Авторизованный пользователь может изменить пароль')
    def test_update_password_with_auth_allows_login_with_new_password(self, registered_user):
        new_password = helpers.generate_random_string(10)

        update_response = UsersApi.update({'password': new_password}, registered_user['token'])
        login_response = UsersApi.login({'email': registered_user['email'], 'password': new_password})

        assert update_response.status_code == 200
        assert update_response.json() == {
            'success': True,
            'user': {'email': registered_user['email'], 'name': registered_user['name']},
        }
        assert login_response.status_code == 200

    @allure.title('Неавторизованный пользователь не может изменить поле')
    @pytest.mark.parametrize('changes', [
        pytest.param({'email': helpers.generate_email()}, id='email'),
        pytest.param({'name': helpers.generate_random_string(10)}, id='имя'),
        pytest.param({'password': helpers.generate_random_string(10)}, id='пароль'),
    ])
    def test_update_field_without_auth_returns_unauthorized(self, changes):
        response = UsersApi.update(changes)

        assert response.status_code == 401
        assert response.json() == data.ERROR_UNAUTHORIZED