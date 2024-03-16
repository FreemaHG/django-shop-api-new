from backend.user_profile.models import Profile
from backend.user_profile.serializers.avatar import ImageSerializer
from backend.user_profile.tests.common_data import CommonTestData


class TestAvatarSerializer(CommonTestData):
    """
    Тестирование схемы для вывода данных об аватарке пользователя
    """

    def test_out_avatar_data(self):
        """
        Проверка возвращаемых данных
        """
        profile = Profile.objects.get(user=self.user)
        control_avatar_str = '/' + str(profile.avatar)

        serializer = ImageSerializer(profile.avatar)

        self.assertEqual(serializer.data['src'], control_avatar_str)
        self.assertEqual(serializer.data['alt'], 'Аватарка пользователя')
        self.assertEqual(len(serializer.data.keys()), 2)
