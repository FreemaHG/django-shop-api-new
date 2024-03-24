import logging

from django.contrib.auth import get_user_model
from django.test import tag

from backend.exceptions import InvalidDataResponseException, NotFoundResponseException
from backend.user_profile.services.profile import ProfileService
from backend.user_profile.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestProfileServices(CommonTestData):
    """
    Тестирование сервиса, отвечающего за вывод и обновление профиля пользователя
    """

    @classmethod
    def setUpTestData(cls):
        """
        Тестовые данные для обновления профайла и пароля
        """
        super().setUpTestData()

        cls.incorrect_update_data_profile = {
            'incorrect_field': 123
        }

        cls.new_user = get_user_model().objects.create_user(
            username='new_user',
            password='test_secret'
        )

    @tag('profile', 'get', 'services')
    def test_get_profile(self):
        """
        Проверка вывода профиля пользователя
        """
        control_fields = ['fullName', 'email', 'phone', 'avatar']

        profile = ProfileService.get(user=self.user)
        fields_list = list(profile.keys())

        self.assertTrue(isinstance(profile, dict))
        self.assertEqual(control_fields, fields_list)

    @tag('profile', 'update', 'services')
    def test_update_profile(self):
        """
        Проверка обновления профиля пользователя
        """
        updated_data = ProfileService.update(user=self.user, data=self.update_data_profile)

        self.assertEqual(updated_data['fullName'], self.update_data_profile['fullName'])
        self.assertEqual(updated_data['email'], self.update_data_profile['email'])
        self.assertEqual(updated_data['phone'], self.update_data_profile['phone'])

    @tag('profile', 'not_found', 'services')
    def test_update_profile_not_found(self):
        """
        Проверка отработки исключения, если профиль для обновления не найден
        """

        self.assertRaises(
            NotFoundResponseException,
            ProfileService.update,
            self.new_user,
            self.update_data_profile
        )

    @tag('profile', 'invalid_data', 'services')
    def test_update_profile_invalid_data(self):
        """
        Проверка отработки исключения при передаче невалидных данных
        """

        self.assertRaises(
            InvalidDataResponseException,
            ProfileService.update,
            self.new_user,
            self.incorrect_update_data_profile
        )
