# Базовый URL сервиса Stellar Burgers
BASE_URL = 'https://stellarburgers.education-services.ru'

# Таймаут запросов, секунды
REQUEST_TIMEOUT = 30

# Пути ручек
REGISTER_PATH = '/api/auth/register'
LOGIN_PATH = '/api/auth/login'
USER_PATH = '/api/auth/user'
INGREDIENTS_PATH = '/api/ingredients'
ORDERS_PATH = '/api/orders'

# Заголовок авторизации
AUTH_HEADER = 'Authorization'

# Тела ответов с ошибками
REGISTER_ERROR_USER_EXISTS = {'success': False, 'message': 'User already exists'}
REGISTER_ERROR_REQUIRED_FIELDS = {'success': False, 'message': 'Email, password and name are required fields'}
LOGIN_ERROR_INCORRECT_DATA = {'success': False, 'message': 'email or password are incorrect'}
ERROR_UNAUTHORIZED = {'success': False, 'message': 'You should be authorised'}
ORDER_ERROR_NO_INGREDIENTS = {'success': False, 'message': 'Ingredient ids must be provided'}

# Текст ответа сервера (HTML) при невалидном хеше ингредиента
ORDER_ERROR_INVALID_HASH_TEXT = 'Internal Server Error'

# Несуществующий хеш ингредиента
INVALID_INGREDIENT_HASH = 'invalidhash123'