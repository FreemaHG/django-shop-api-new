import copy
import json

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class CommonTestData(APITestCase):
    """
    Общие данные, используемые для тестов
    """

    @classmethod
    def setUpTestData(cls):
        """
        Тестовые данные для проверки регистрации и авторизации пользователя
        """

        cls.empty_data = {
            '': ''
        }

        cls.login_data = {
            'username': 'test_user',
            'password': 'secret_password'
        }

        cls.registration_data = cls.login_data
        cls.registration_data['name'] = 'Васильев Василий Васильевич'
        cls.double_registration_data = copy.deepcopy(cls.registration_data)
        cls.double_registration_data['username'] = 'double_test_user'

        cls.login_data_json = json.dumps(cls.login_data)
        cls.registration_data_json = json.dumps(cls.registration_data)

        cls.new_user = get_user_model().objects.create_user(
            username='double_test_user',
            password='test_secret'
        )

        cls.invalid_registration_data = {
            'name': 123,
            'username': 321
        }
