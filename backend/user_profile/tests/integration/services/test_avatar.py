from django.contrib.auth import get_user_model
from django.test import tag

from backend.user_profile.models import Profile
from backend.user_profile.serializers.avatar import ImageSerializer
from backend.user_profile.services.avatar import AvatarService
from backend.user_profile.tests.common_data import CommonTestData


class TestPasswordServices(CommonTestData):
    """
    Тестирование сервиса, отвечающего за обновление аватара пользователя
    """

    @tag('avatar', 'update')
    def test_update_avatar(self):
        """
        Проверка обновления аватара пользователя
        """

        avatar_data = AvatarService.update(user=self.user, avatar=self.avatar_name)
        serializer = ImageSerializer(data=avatar_data)

        profile = Profile.objects.get(user=self.user)

        self.assertEqual(profile.avatar.__str__(), self.avatar_name)
        self.assertTrue(serializer.is_valid())
        self.assertTrue(isinstance(avatar_data, dict))

    @tag('avatar', 'error')
    def test_update_avatar_error(self):
        """
        Проверка ответа при обновлении аватара в несуществующем профиле
        """

        new_user = get_user_model().objects.create_user(
            username='new_user',
            password='test_secret'
        )

        result = AvatarService.update(user=new_user, avatar=self.avatar_name)
        self.assertFalse(result)
