from django.test import tag
from django.urls import reverse
from rest_framework import status

from backend.user_profile.tests.common_data import CommonTestData


class TestUrlsName(CommonTestData):
    """
    Тестирование доступности url-адресов по urlname
    """

    @tag('profile', 'urls')
    def test_profile_urlname(self):
        """
        Проверка доступности профиля
        """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('profile', 'update', 'urls')
    def test_profile_update_urlname(self):
        """
        Проверка обновления профиля
        """
        response = self.client.post(reverse('profile'), data=self.update_data_profile)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('avatar', 'update', 'urls')
    def test_update_avatar_urlname(self):
        """
        Проверка обновления аватара
        """
        data = {'avatar': self.avatar}
        response = self.client.post(reverse('update-avatar'), data=data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @tag('password', 'update', 'urls')
    def test_update_password_urlname(self):
        """
        Проверка обновления пароля
        """
        response = self.client.post(reverse('update-password'), data=self.update_data_password)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.delete_test_avatar()
