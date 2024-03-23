from django.test import tag
from django.urls import reverse
from rest_framework import status

from backend.user_auth.tests.common_data import CommonTestData


class TestUrlsName(CommonTestData):
    """
    Тестирование доступности url-адресов по urlname
    """

    @tag('registration')
    def test_profile_urlname(self):
        """
        Проверка доступности URL для регистрации
        """

        response = self.client.post(
            reverse('sign-up'),
            data=self.registration_data_json,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
