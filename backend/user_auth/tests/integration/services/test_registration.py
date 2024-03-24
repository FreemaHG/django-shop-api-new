from django.test import tag

from backend.exceptions import InvalidDataResponseException
from backend.user_auth.services.registration import RegistrationService
from backend.user_auth.tests.common_data import CommonTestData


class TestRegistrationServices(CommonTestData):
    """
    Тестирование сервиса, отвечающего за регистрацию нового пользователя
    """

    @tag('registration', 'services')
    def test_registration_user(self):
        """
        Проверка возвращения зарегистрированного и аутентифицированного пользователя
        """

        new_user = RegistrationService.registration(data=self.registration_data)

        self.assertTrue(new_user)
        self.assertTrue(new_user.is_authenticated)

    @tag('registration', 'error', 'services')
    def test_already_created_user(self):
        """
        Проверка отработки исключения при регистрации пользователя с уже имеющимся в БД username
        """

        self.assertRaises(
            InvalidDataResponseException,
            RegistrationService.registration,
            self.double_registration_data
        )

    @tag('registration', 'invalid_data', 'services')
    def test_invalid_data(self):
        """
        Проверка отработки исключения при передаче невалидных данных
        """

        self.assertRaises(
            InvalidDataResponseException,
            RegistrationService.registration,
            self.invalid_registration_data
        )
