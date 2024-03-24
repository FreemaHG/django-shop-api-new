from django.test import tag

from backend.user_auth.serializers import RegisterSerializer
from backend.user_auth.tests.common_data import CommonTestData


class TestRegisterSerializer(CommonTestData):
    """
    Тестирование схемы для регистрации пользователя
    """

    @tag('registration', 'serializers')
    def test_registration(self):
        """
        Передача и проверка валидных данных
        """
        serializer = RegisterSerializer(data=self.registration_data)

        self.assertTrue(serializer.is_valid())

    @tag('registration', 'error', 'serializers')
    def test_no_required_fields(self):
        """
        Проверка отработки исключения при отсутствии обязательных полей
        """
        serializer = RegisterSerializer(data=self.empty_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['name'][0], 'Обязательное поле.')
