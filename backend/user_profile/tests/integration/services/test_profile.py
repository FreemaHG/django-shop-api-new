import logging

from django.contrib.auth import get_user_model
from django.test import tag

from backend.user_profile.serializers.profile import ProfileOutSerializer
from backend.user_profile.services.profile import ProfileService
from backend.user_profile.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestProfileServices(CommonTestData):
    """
    Тестирование сервиса, отвечающего за вывод и обновление профиля пользователя
    """

    @classmethod
    def setUpTestData(self):
        """
        Тестовые данные для обновления профайла и пароля
        """
        super().setUpTestData()

        self.incorrect_update_data_profile = {
            'incorrect_field': 123
        }

        self.new_user = get_user_model().objects.create_user(
            username='new_user',
            password='test_secret'
        )

    @tag('profile', 'get')
    def test_get_profile(self):
        """
        Тестирование вывода профиля пользователя
        """
        control_fields = ['fullName', 'email', 'phone', 'avatar']

        profile = ProfileService.get(user=self.user)
        fields_list = list(profile.fields.keys())

        self.assertTrue(isinstance(profile, ProfileOutSerializer))
        self.assertEqual(control_fields, fields_list)

    @tag('profile', 'not_found')
    def test_get_profile_not_found(self):
        """
        Тестирование возвращаемых данных при отсутствии профиля пользователя
        """
        result = ProfileService.get(user=self.new_user)
        self.assertEqual(result, None)

    @tag('profile', 'update')
    def test_update_profile(self):
        """
        Тестирование обновление профиля пользователя
        """
        updated_data = ProfileService.update(user=self.user, data=self.update_data_profile)

        self.assertEqual(updated_data['fullName'], self.update_data_profile['fullName'])
        self.assertEqual(updated_data['email'], self.update_data_profile['email'])
        self.assertEqual(updated_data['phone'], self.update_data_profile['phone'])

    @tag('profile', 'not_found')
    def test_update_profile_not_found(self):
        """
        Тестирование ответа, если профиль для обновления не найден
        """
        result = ProfileService.update(user=self.new_user, data=self.update_data_profile)
        self.assertEqual(result, None)

    @tag('profile', 'invalid_data')
    def test_update_profile_invalid_data(self):
        """
        Тестирование ответа при передаче невалидных данных
        """
        result = ProfileService.update(user=self.new_user, data=self.incorrect_update_data_profile)

        self.assertFalse(result)
