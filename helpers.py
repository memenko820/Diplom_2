import random
import string

import data


def generate_random_string(length):
    # Строка из букв нижнего регистра заданной длины
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_user_payload():
    # Данные для регистрации нового пользователя
    return {
        'email': f'{generate_random_string(10)}@yandex.ru',
        'password': generate_random_string(10),
        'name': generate_random_string(10),
    }


def remove_field(payload, field):
    # Копия словаря без указанного поля
    return {key: value for key, value in payload.items() if key != field}


def build_auth_headers(token):
    # Заголовки с токеном; без токена заголовков авторизации нет
    return {data.AUTH_HEADER: token} if token else {}


def generate_email():
    # Уникальный email для тестового пользователя
    return f'{generate_random_string(10)}@yandex.ru'


def generate_user_payload():
    # Данные для регистрации нового пользователя
    return {
        'email': generate_email(),
        'password': generate_random_string(10),
        'name': generate_random_string(10),
    }


def get_credentials(user):
    # Только поля, нужные для логина
    return {'email': user['email'], 'password': user['password']}


def extract_values(items, key):
    # Список значений указанного поля из списка словарей
    return [item[key] for item in items]