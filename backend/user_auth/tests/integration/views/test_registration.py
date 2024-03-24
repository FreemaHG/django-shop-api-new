from django.contrib.auth.models import User
from django.test import tag
from rest_framework import status

from backend.user_auth.tests.common_data import CommonTestData


class TestRegistrationViews(CommonTestData):
    """
    Тестирование представления, отвечающего за регистрацию пользователя
    """

    @tag('post', 'registration', 'views')
    def test_registration_user(self):
        """
        Проверка успешной регистрации и авторизации пользователя
        """

        response = self.client.post('/api/sign-up/', data=self.registration_data, format='json')
        user = User.objects.get(username=self.registration_data['username'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user.is_authenticated)

    @tag('registration', 'post', 'error', 'views')
    def test_already_registration_user(self):
        """
        Проверка статуса ответа при регистрации пользователя с уже имеющимся в БД username
        """

        response = self.client.post('/api/sign-up/', data=self.double_registration_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Пользователь с таким именем уже зарегистрирован')

    @tag('registration', 'post', 'invalid_data', 'views')
    def test_invalid_registration_user_data(self):
        """
        Проверка статуса ответа при попытке зарегистрироваться с невалидными данными
        """

        response = self.client.post('/api/sign-up/', data=self.invalid_registration_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data['password'][0], 'Обязательное поле.')
