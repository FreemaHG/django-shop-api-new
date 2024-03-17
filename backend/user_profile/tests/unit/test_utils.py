import os

from django.test import tag

from backend.user_profile.models import Profile
from backend.user_profile.tests.common_data import CommonTestData
from backend.user_profile.utils.save_file import AVATARS_PATH, avatar_path


class TestUtils(CommonTestData):
    """
    Тестирование утилит приложения
    """

    @tag('avatar')
    def test_save_avatar_path(self):
        """
        Проверка корректности составления директории для сохранения аватарок пользователя
        """
        avatar_name = 'test_avatar.png'
        profile = Profile.objects.get(id=1)
        control_path = os.path.join(AVATARS_PATH, str(profile.id), avatar_name)

        path = avatar_path(instance=profile, filename=avatar_name)

        self.assertEqual(control_path, path)
        self.delete_test_avatar()
