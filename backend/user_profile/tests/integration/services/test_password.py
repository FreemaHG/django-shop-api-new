from backend.user_profile.services.password import PasswordService
from backend.user_profile.tests.common_data import CommonTestData


class TestPasswordServices(CommonTestData):
    """
    Тестирование сервиса, отвечающего за обновление пароля от личного кабинета пользователя
    """

    def test_update_password(self):
        """
        Проверка обновления пароля
        """
        old_password = self.user.password
        new_password = self.update_data_password['password']

        updated_user = PasswordService.update(user=self.user, data=self.update_data_password)

        self.assertTrue(updated_user.is_authenticated)  # Проверяем, что пользователь аутентифицирован
        self.assertNotEqual(old_password, updated_user.password)  # Проверяем, что старый пароль не равен новому
        self.assertFalse(self.user.check_password(old_password))  # Проверяем, что старый пароль больше не действителен
        self.assertTrue(self.user.check_password(new_password))  # Проверяем, что новый пароль установлен корректно

    def test_invalid_data(self):
        """
        Проверка ответа при передаче невалидных данных
        """

        result = PasswordService.update(user=self.user, data=self.incorrect_update_data_password)
        self.assertFalse(result)
