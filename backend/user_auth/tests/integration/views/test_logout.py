import logging

from django.contrib.auth.models import User
from django.test import tag
from rest_framework import status

from backend.user_auth.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestRegistrationViews(CommonTestData):
    """
    Тестирование представления, отвечающего за выход пользователя
    """

    @tag('logout', 'views', 'exception')
    def test_logout_for_anonymous_user(self):
        """
        Проверка ответа при выходе неавторизованного пользователя
        """

        response = self.client.post('/api/sign-out/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('logout', 'views')
    def test_logout(self):
        """
        Проверка представления для выхода из учетной записи
        """

        user = User.objects.get(username='double_test_user')
        self.client.force_login(user=user)

        # Проверка, что id сессии записан (пользователь авторизован)
        self.assertIn('_auth_user_id', self.client.session)

        response = self.client.post('/api/sign-out/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверка, что id сессии удален (пользователь не авторизован)
        self.assertNotIn('_auth_user_id', self.client.session)
