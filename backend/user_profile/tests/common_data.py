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
    def setUpTestData(cls):
        """
        Тестовые данные для обновления профайла и пароля
        """

        cls.control_full_name = 'Васильев Василий Васильевич'

        cls.update_data_profile = {
            'fullName': 'Валентин Валентинов Валентинович',
            'phone': '89027448562',
            'email': 'updated_tester@example.com'
        }

        cls.update_data_password = {
            'password': 'new_secret_password',
            'passwordReply': 'new_secret_password'
        }

        cls.incorrect_update_data_password = {
            'password': 'new_secret_password',
            'passwordReply': 'secret_password'
        }

        test_img = open(os.path.join('backend', 'user_profile', 'tests', 'files', 'test_avatar.png'), 'rb').read()
        cls.avatar_name = 'test_avatar.png'
        cls.avatar = SimpleUploadedFile(name=cls.avatar_name, content=test_img, content_type='image/jpeg')

        cls.user = User.objects.get(username='test_user')

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

        delete_file = os.path.join(MEDIA_ROOT, AVATARS_PATH, str(self.user.id), avatar_name)

        try:
            os.remove(delete_file)

        except FileNotFoundError:
            logger.error(f'Файл для удаления не найден: {delete_file}')
