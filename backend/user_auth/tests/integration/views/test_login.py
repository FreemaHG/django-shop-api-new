from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import tag
from rest_framework import status

from backend.user_auth.tests.common_data import CommonTestData


class TestRegistrationViews(CommonTestData):
    """
    Тестирование представления, отвечающего за авторизацию пользователя
    """

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.user = get_user_model().objects.create_user(
            username='test_user',
            password='secret_password'
        )

    @tag('post', 'login', 'views')
    def test_login_user(self):
        """
        Проверка успешной авторизации пользователя
        """

        response = self.client.post('/api/sign-in/', data=self.login_data, format='json')
        user = User.objects.get(username=self.login_data['username'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(user.is_authenticated)

    @tag('post', 'login', 'views', 'exception')
    def test_login_or_password_mismatch(self):
        """
        Проверка ответа при несоответствии логина или пароля
        """

        response = self.client.post('/api/sign-in/', data=self.random_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @tag('post', 'login', 'views', 'invalid_data')
    def test_invalid_datah(self):
        """
        Проверка ответа при передаче невалидны данных
        """

        response = self.client.post('/api/sign-in/', data=self.empty_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
