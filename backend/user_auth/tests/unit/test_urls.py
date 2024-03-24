import json
import logging

from django.test import tag
from django.urls import reverse
from rest_framework import status

from backend.user_auth.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestUrlsName(CommonTestData):
    """
    Тестирование доступности url-адресов по urlname
    """

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.registration_data = {
            'username': 'new_user',
            'password': 'secret_password',
            'name': 'Васильев Василий Васильевич'
        }

        cls.login_data = {
            'username': 'double_test_user',
            'password': 'test_secret'
        }

    @tag('registration', 'urls')
    def test_registration_urlname(self):
        """
        Проверка доступности URL для регистрации
        """

        response = self.client.post(
            reverse('sign-up'),
            data=json.dumps(self.registration_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @tag('login', 'urls')
    def test_login_urlname(self):
        """
        Проверка доступности URL для авторизации
        """

        response = self.client.post(
            reverse('sign-in'),
            data=json.dumps(self.login_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('logout', 'urls')
    def test_logout_urlname(self):
        """
        Проверка доступности URL для выхода из учетной записи
        """

        self.client.force_authenticate(user=self.new_user)
        response = self.client.post(reverse('sign-out'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
