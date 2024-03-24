from django.contrib.auth import get_user_model
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

    @tag('get', 'profile', 'repositories')
    def test_get_profile(self):
        """
        Проверка корректности поиска и возврата профиля пользователя
        """
        user = User.objects.get(id=1)
        control_profile = Profile.objects.get(id=1)

        profile = ProfileRepository.get(user=user)

        self.assertTrue(isinstance(profile, Profile))
        self.assertEqual(control_profile, profile)

    @tag('create', 'profile', 'repositories')
    def test_create_profile(self):
        """
        Проверка корректности создания профиля пользователя
        """
        new_user = get_user_model().objects.create_user(
            username='new_user',
            password='test_secret'
        )

        new_profile = ProfileRepository.create(user=new_user)

        self.assertTrue(isinstance(new_profile, Profile))
        self.assertEqual(new_profile.user, new_user)
