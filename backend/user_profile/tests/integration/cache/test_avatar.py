from django.core.cache import cache
from django.test import tag

from backend.user_profile.services.avatar import AvatarService
from backend.user_profile.tests.common_data import CommonTestData


class TestCacheAvatar(CommonTestData):
    """
    Тестирование кэширования при обновлении аватара пользователя
    """

    @tag('cache', 'avatar')
    def test_delete_cache(self):
        """
        Проверка очистки данных в кэше при обновлении аватара
        """

        AvatarService.update(user=self.user, avatar=self.avatar_name)
        cached_data = cache.get('profile')

        self.assertFalse(cached_data)
