from django.test import tag
from rest_framework import status
from rest_framework.test import APIClient

from backend.user_profile.tests.common_data import CommonTestData


class TestPasswordViews(CommonTestData):
    """
    Тестирование представлений, отвечающих за обновление пароля пользователя
    """

    @tag('update', 'password', 'anonymous')
    def test_update_password_for_anonymous(self):
        """
        Проверка ответа при попытке обновить пароль неавторизованным пользователем
        """
        client = APIClient()
        response = client.post('/api/profile/password/', data=self.update_data_password)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('update', 'password')
    def test_update_password(self):
        """
        Проверка обновления пароля
        """
        response = self.client.post('/api/profile/password/', data=self.update_data_password)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('update', 'password', 'invalid_data')
    def test_update_password_invalid_data(self):
        """
        Проверка ответа при передаче невалидных данных
        """
        response = self.client.post('/api/profile/password/', data=self.incorrect_update_data_password)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
