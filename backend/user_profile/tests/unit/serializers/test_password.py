from django.test import tag

from backend.user_profile.serializers.password import PasswordSerializer
from backend.user_profile.tests.common_data import CommonTestData


class TestPasswordSerializer(CommonTestData):
    """
    Тестирование схемы для обновления пароля пользователя
    """

    @tag('password')
    def test_validate(self):
        """
        Проверка валидатора, сравнивающего пароли
        """
        serializer = PasswordSerializer(data=self.update_data_password)
        self.assertTrue(serializer.is_valid())

    @tag('password', 'error')
    def test_validate_error(self):
        """
        Проверка отработки уведомления о невалидных данных
        """
        serializer = PasswordSerializer(data=self.incorrect_update_data_password)

        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
        self.assertEqual(serializer.errors['non_field_errors'][0], 'Пароли не совпадают')
