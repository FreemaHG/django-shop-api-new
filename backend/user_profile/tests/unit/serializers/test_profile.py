from backend.user_profile.models import Profile
from backend.user_profile.serializers.profile import ProfileOutSerializer
from backend.user_profile.tests.common_data import CommonTestData


class TestProfileSerializer(CommonTestData):
    """
    Тестирование схемы для вывода данных профиля
    """

    def test_out_data(self):
        """
        Проверка возвращаемых данных
        """
        profile = Profile.objects.get(user=self.user)

        control_full_name = 'Васильев Василий Васильевич'
        control_avatar_str = '/' + profile.avatar.__str__()

        serializer = ProfileOutSerializer(profile)
        avatar_data_dict = dict(serializer.data['avatar'])
        fields_list = list(serializer.data.keys())

        self.assertEqual(serializer.data['fullName'], control_full_name)
        self.assertEqual(serializer.data['email'], profile.user.email)
        self.assertEqual(serializer.data['phone'], profile.phone)
        self.assertEqual(avatar_data_dict['src'], control_avatar_str)
        self.assertEqual(avatar_data_dict['alt'], 'Аватарка пользователя')
        self.assertEqual(4, len(fields_list))
