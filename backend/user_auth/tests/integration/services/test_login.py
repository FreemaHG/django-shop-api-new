from django.contrib.auth import get_user_model
from django.test import tag

from backend.exceptions import InvalidDataResponseException
from backend.user_auth.services.login import LoginService
from backend.user_auth.tests.common_data import CommonTestData


class TestLoginServices(CommonTestData):
    """
    Тестирование сервиса, отвечающего за авторизацию пользователя
    """

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.user = get_user_model().objects.create_user(
            username='test_user',
            password='secret_password'
        )

    @tag('login', 'services')
    def test_login_user(self):
        """
        Проверка авторизации пользователя
        """
        authenticated_user = LoginService.login(data=self.login_data)

        self.assertEqual(authenticated_user, self.user)

    @tag('login', 'exception', 'services')
    def test_login_or_password_mismatch(self):
        """
        Проверка ответа при передаче неподходящих логина и пароля
        """

        self.assertRaises(
            InvalidDataResponseException,
            LoginService.login,
            self.random_data
        )

    @tag('login', 'exception', 'services')
    def test_invalid_data(self):
        """
        Проверка ответа при передаче невалидных данных
        """

        self.assertRaises(
            InvalidDataResponseException,
            LoginService.login,
            self.empty_data
        )
