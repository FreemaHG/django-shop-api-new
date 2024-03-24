from django.test import tag

from backend.user_auth.business.user_registration import RegistrationUserBusiness
from backend.user_auth.tests.common_data import CommonTestData


class TestBusiness(CommonTestData):
    """
    Тестирование бизнес-логики приложения по регистрации нового пользователя
    """

    @classmethod
    def setUpTestData(cls):
        """
        Тестовые данные для проверки регистрации и авторизации пользователя
        """
        super().setUpTestData()
        cls.last_name, cls.first_name, cls.patronymic = cls.registration_data['name'].split(' ')

    @tag('registration', 'business')
    def test_save_basic_data(self):
        """
        Проверка корректности сохранения основных данных: username, профиля и пароля
        """
        self.new_user = RegistrationUserBusiness.registration(data=self.registration_data)

        self.assertTrue(self.new_user.profile)
        self.assertEqual(self.new_user.username, self.registration_data['username'])
        self.assertTrue(self.new_user.check_password(self.registration_data['password']))

    @tag('registration', 'business')
    def test_registration_user_with_unnecessary_words(self):
        """
        Проверка корректности сохранения полного имени нового пользователя при передаче 4 и более слов в имени
        """
        self.registration_data['name'] = 'Васильев Василий Васильевич Василькович'
        self.new_user = RegistrationUserBusiness.registration(data=self.registration_data)

        self.assertEqual(self.new_user.first_name, self.first_name)
        self.assertEqual(self.new_user.last_name, self.last_name)
        self.assertEqual(self.new_user.profile.patronymic, self.patronymic)

    @tag('registration', 'business')
    def test_registration_user_with_full_name(self):
        """
        Проверка корректности сохранения полного имени нового пользователя
        """
        self.new_user = RegistrationUserBusiness.registration(data=self.registration_data)

        self.assertEqual(self.new_user.first_name, self.first_name)
        self.assertEqual(self.new_user.last_name, self.last_name)
        self.assertEqual(self.new_user.profile.patronymic, self.patronymic)

    @tag('registration', 'business')
    def test_registration_user_with_first_and_last_names(self):
        """
        Проверка корректности сохранения имени и фамилии нового пользователя
        """
        self.registration_data['name'] = 'Васильев Василий'
        self.new_user = RegistrationUserBusiness.registration(data=self.registration_data)

        self.assertEqual(self.new_user.first_name, self.first_name)
        self.assertEqual(self.new_user.last_name, self.last_name)
        self.assertFalse(self.new_user.profile.patronymic)

    @tag('registration', 'business')
    def test_registration_user_with_first_names(self):
        """
        Проверка корректности сохранения имени нового пользователя
        """
        self.registration_data['name'] = 'Василий'
        self.new_user = RegistrationUserBusiness.registration(data=self.registration_data)

        self.assertEqual(self.new_user.first_name, self.first_name)
        self.assertFalse(self.new_user.last_name)
        self.assertFalse(self.new_user.profile.patronymic)
