from django.contrib.auth.models import User
from django.test import tag
from rest_framework.test import APITestCase

from backend.user_profile.models import Profile
from backend.user_profile.repositories.profile import ProfileRepository
from backend.user_profile.tests.common_data import FIXTURES_PATH


class TestRepositories(APITestCase):
    """
    Тестирование метода по чтению профиля пользователя
    """

    fixtures = [FIXTURES_PATH]

    @tag('get', 'profile')
    def test_get_profile(self):
        """
        Проверка корректности поиска и возврата профиля пользователя
        """
        user = User.objects.get(id=1)
        control_profile = Profile.objects.get(id=1)

        profile = ProfileRepository.get(user=user)

        self.assertEqual(control_profile, profile)