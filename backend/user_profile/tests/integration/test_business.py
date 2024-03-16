from backend.user_profile.business.update_profile import ProfileUpdateBusiness
from backend.user_profile.models import Profile
from backend.user_profile.tests.common_data import CommonTestData


class TestBusiness(CommonTestData):
    """
    Тестирование бизнес-логики приложения по обновлению данных профиля пользователя
    """

    def test_update_profile(self):
        """
        Проверка корректности обновления данных профиля и пользователя
        """

        last_name, first_name, patronymic = self.update_data_profile['fullName'].split(' ')
        profile = Profile.objects.get(id=1)

        updated_profile = ProfileUpdateBusiness.update(profile=profile, data=self.update_data_profile)
        updated_user = updated_profile.user

        self.assertEqual(updated_profile.patronymic, patronymic)
        self.assertEqual(updated_profile.phone, self.update_data_profile['phone'])

        self.assertEqual(updated_user.first_name, first_name)
        self.assertEqual(updated_user.last_name, last_name)
        self.assertEqual(updated_user.email, self.update_data_profile['email'])
