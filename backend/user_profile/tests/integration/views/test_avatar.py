import logging
import os

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient

from backend.user_profile.tests.common_data import CommonTestData

logger = logging.getLogger(__name__)


class TestAvatarViews(CommonTestData):
    """
    Тестирование представлений, отвечающих за обновление аватара пользователя
    """

    @classmethod
    def setUpTestData(self):
        super().setUpTestData()

        self.new_user = get_user_model().objects.create_user(
            username='new_user',
            password='test_secret'
        )

        update_img = open(os.path.join('backend', 'user_profile', 'tests', 'files', 'update_avatar.jpg'), 'rb').read()

        self.update_avatar_name = 'update_avatar.png'
        self.update_avatar = SimpleUploadedFile(name=self.update_avatar_name,
                                                content=update_img, content_type='image/jpeg')
        self.update_data = {'avatar': self.update_avatar}

    def test_update_avatar_for_anonymous(self):
        """
        Проверка ответа при попытке обновить аватар неавторизованным пользователем
        """
        client = APIClient()
        response = client.post('/api/profile/avatar/', data=self.update_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Удаляем аватарку с физического накопителя
        self.delete_test_avatar(avatar_name=self.update_avatar_name)

    def test_update_avatar(self):
        """
        Проверка обновления аватара пользователя
        """
        response = self.client.post('/api/profile/avatar/', data=self.update_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_avatar_error(self):
        """
        Проверка ответа при попытке обновить аватар несуществующего профиля
        """
        client = APIClient()
        client.force_authenticate(user=self.new_user)
        response = client.post('/api/profile/avatar/', data=self.update_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
