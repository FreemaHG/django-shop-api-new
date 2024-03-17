from django.core.cache import cache
from django.test import tag

from backend.user_profile.services.profile import ProfileService
from backend.user_profile.tests.common_data import CommonTestData


class TestCacheProfile(CommonTestData):
    """
    Тестирование кэширования при возврате и обновлении профиля пользователя
    """

    @tag('cache', 'profile')
    def test_set_cache(self):
        """
        Проверка сохранения данных в кэше
        """

        profile_data = ProfileService.get(user=self.user)

        cached_data = cache.get('profile')

        self.assertTrue(cached_data)
        self.assertEqual(cached_data, profile_data)

    @tag('cache', 'profile')
    def test_delete_cache(self):
        """
        Проверка очистки данных в кэше при обновлении профиля пользователя
        """

        ProfileService.update(user=self.user, data=self.update_data_profile)
        cached_data = cache.get('profile')

        self.assertFalse(cached_data)
