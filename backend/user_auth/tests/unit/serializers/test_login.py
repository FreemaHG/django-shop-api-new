import logging

from django.test import tag

from backend.user_auth.serializers import LoginSerializer
from backend.user_auth.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestLoginSerializer(CommonTestData):
    """
    Тестирование схемы для авторизации пользователя
    """

    @tag('login', 'serializers')
    def test_login(self):
        """
        Передача и проверка валидных данных
        """
        serializer = LoginSerializer(data=self.registration_data)

        self.assertTrue(serializer.is_valid())

    @tag('login', 'error', 'serializers')
    def test_no_required_fields(self):
        """
        Проверка отработки исключения при отсутствии обязательных полей
        """
        serializer = LoginSerializer(data=self.empty_data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['username'][0], 'Обязательное поле.')
        self.assertEqual(serializer.errors['password'][0], 'Обязательное поле.')
