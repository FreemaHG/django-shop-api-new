import json
import logging

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from backend.user_profile.models import Profile
from backend.user_profile.serializers.profile import ProfileOutSerializer
from backend.user_profile.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestProfileViews(CommonTestData):
    """
    Тестирование представлений, отвечающих за вывод и обновление профиля пользователя
    """

    @classmethod
    def setUpTestData(self):
        """
        Тестовые данные для обновления профайла и пароля
        """
        super().setUpTestData()

        self.new_user = get_user_model().objects.create_user(
            username='new_user',
            password='test_secret'
        )

    def test_get_profile_for_auth_user(self):
        """
        Проверка доступности профиля для авторизованного пользователя
        """
        profile = Profile.objects.get(user=self.user)
        serializer = ProfileOutSerializer(profile)
        control_result = json.dumps(serializer.data, ensure_ascii=False)

        response = self.client.get('/api/profile/')
        result = json.dumps(response.json(), ensure_ascii=False)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(control_result, result)

    def test_get_profile_for_anonymous(self):
        """
        Проверка недоступности профиля для неавторизованного пользователя
        """
        client = APIClient()
        response = client.get('/api/profile/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_profile_not_found(self):
        """
        Проверка ответа при отсутствии профиля пользователя
        """
        self.client.force_authenticate(user=self.new_user)
        response = self.client.get('/api/profile/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_profile_for_auth_user(self):
        """
        Проверка обновления профиля для авторизованного пользователя
        """
        response = self.client.post('/api/profile/', data=self.update_data_profile)
        response_json = response.json()
        result = json.dumps(response_json, ensure_ascii=False)

        updated_profile = Profile.objects.get(user=self.user)
        serializer = ProfileOutSerializer(updated_profile)
        control_result = json.dumps(serializer.data, ensure_ascii=False)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(control_result, result)
        self.assertEqual(response_json['fullName'], self.update_data_profile['fullName'])
        self.assertEqual(response_json['email'], self.update_data_profile['email'])
        self.assertEqual(response_json['phone'], self.update_data_profile['phone'])

    def test_update_profile_for_anonymous(self):
        """
        Проверка ответа при попытке обновить профиль для неавторизованного пользователя
        """
        client = APIClient()
        response = client.post('/api/profile/', data=self.update_data_profile)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_profile_not_found(self):
        """
        Проверка ответа при попытке обновить несуществующий профиль
        """
        self.client.force_authenticate(user=self.new_user)
        response = self.client.post('/api/profile/', data=self.update_data_profile)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_profile_with_incorrect_data(self):
        """
        Проверка ответа при попытке обновить профиль невалидными данными
        """
        response = self.client.post('/api/profile/', data=self.incorrect_update_data_password)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
