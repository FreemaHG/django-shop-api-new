import logging
import os

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase

from backend.megano.settings import BASE_DIR, MEDIA_ROOT
from backend.user_profile.utils.save_file import AVATARS_PATH

logger = logging.getLogger(__name__)

FIXTURES_PATH = os.path.join(BASE_DIR, 'backend', 'user_profile', 'tests', 'fixtures', 'profile_data.json')


class CommonTestData(APITestCase):
    """
    Общие данные, используемые во всех тестах
    """

    fixtures = [FIXTURES_PATH]

    @classmethod
    def setUpTestData(self):
        """
        Тестовые данные для обновления профайла и пароля
        """

        self.update_data_profile = {
            'fullName': 'Валентин Валентинов Валентинович',
            'phone': '89027448562',
            'email': 'updated_tester@example.com'
        }

        self.update_data_password = {
            'password': 'new_secret_password',
            'passwordReply': 'new_secret_password'
        }

        self.incorrect_update_data_password = {
            'password': 'new_secret_password',
            'passwordReply': 'secret_password'
        }

        test_img = open(os.path.join('backend', 'user_profile', 'tests', 'files', 'test_avatar.png'), 'rb').read()
        self.avatar_name = 'test_avatar.png'
        self.avatar = SimpleUploadedFile(name=self.avatar_name, content=test_img, content_type='image/jpeg')

        self.user = User.objects.get(username='test_user')

    def setUp(self):
        """
        Создаем сеанс аутентификации для пользователя, созданного из фикстур
        """
        self.client.force_authenticate(user=self.user)

    def delete_test_avatar(self, avatar_name: str | None = None):
        """
        Удаление изображений с диска после окончания тестов
        """
        if avatar_name is None:
            avatar_name = self.avatar_name

        os.remove(os.path.join(MEDIA_ROOT, AVATARS_PATH, str(self.user.id), avatar_name))
