from django.http import QueryDict
from django.test import tag

from backend.user_auth.tests.common_data import CommonTestData
from backend.user_auth.utils import reading_data_from_request


class TestUtils(CommonTestData):
    """
    Тестирование утилит приложения
    """

    @classmethod
    def setUpTestData(cls):
        cls.control_result = {
            'username': 'admin',
            'password': 'admin1'
        }

    @tag('registration', 'login', 'utils')
    def test_reading_data_from_request_with_querydict(self):
        """
        Проверка корректности извлечения данных из запроса при регистрации и авторизации пользователя
        """
        raw_data = QueryDict('{"username":"admin","password":"admin1"}')
        result = reading_data_from_request(raw_data=raw_data)

        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result, self.control_result)

    @tag('registration', 'login', 'utils')
    def test_reading_data_from_request_with_dict(self):
        """
        Проверка корректности извлечения данных из запроса при регистрации и авторизации пользователя
        """
        raw_data = {'username': 'admin', 'password': 'admin1'}
        result = reading_data_from_request(raw_data=raw_data)

        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result, self.control_result)
