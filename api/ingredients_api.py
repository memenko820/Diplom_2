import allure
import requests

import data


class IngredientsApi:

    @staticmethod
    @allure.step('Получение списка ингредиентов')
    def get_ingredients():
        return requests.get(f'{data.BASE_URL}{data.INGREDIENTS_PATH}', timeout=data.REQUEST_TIMEOUT)