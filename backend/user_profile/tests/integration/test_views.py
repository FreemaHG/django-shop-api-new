import logging

# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from backend.user_profile.models import Profile

logger = logging.getLogger(__name__)


# class TestViews(APITestCase):
#     """
#     Тестирование представлений
#     """
#
#     @classmethod
#     def setUpTestData(cls):
#         """
#         Тестовые пользователь и профайл
#         """
#
#         cls.test_user = User.objects.create_user(
#             username='test_user',
#             first_name='First',
#             last_name='Second',
#             email='tester@gmail.com',
#             password='secret_password'
#         )
#
#         cls.test_profile = Profile.objects.create(
#             user=cls.test_user,
#             patronymic='Third',
#             phone='89027448560'
#         )
#
#     def test_profile_url_for_auth_user(self):
#         """
#         Проверка доступности профиля для авторизованного пользователя
#         """
#         self.client.force_login(user=self.test_user)
#         response = self.client.get('/api/profile/')
#         # logger.info(f'response: {response.json()}')
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_profile_url_for_anonymous(self):
#         """
#         Проверка доступности профиля для неавторизованного пользователя
#         """
#         response = self.client.get('/api/profile/')
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#
# class TestUrlsName(APITestCase):
#     """
#     Проверка доступности url-адресов по urlname
#     """
#
#     fixtures = [FIXTURES_PATH]
#
#     @classmethod
#     def setUpTestData(cls):
#         """
#         Тестовые пользователь и профайл
#         """
#
#         # cls.test_user = User.objects.create_user(
#         #     username='test_user',
#         #     first_name='Василий',
#         #     last_name='Васильев',
#         #     email='tester@example.com',
#         #     password='secret_password'
#         # )
#         #
#         # cls.test_img = open(os.path.join('backend', 'user_profile', 'tests', 'files', 'test_avatar.png'), 'rb').read()
#         # cls.avatar_name = 'test_avatar.png'
#         # cls.test_img_obj = SimpleUploadedFile(name=cls.avatar_name, content=cls.test_img, content_type='image/jpeg')
#         #
#         # cls.test_profile = Profile.objects.create(
#         #     user=cls.test_user,
#         #     patronymic='Васильевич',
#         #     phone='89027448560',
#         #     avatar=cls.test_img_obj
#         # )
#
#         cls.update_data_profile = {
#             "fullName": "Валентин Валентинов Валентинович",
#             "phone": "89027448562",
#             "email": "updated_tester@example.com"
#         }
#
#         cls.update_data_password = {
#             'password': 'new_secret_password',
#             'passwordReply': 'new_secret_password'
#         }
#
#     # def delete_test_avatar(self):
#     #     shutil.rmtree(os.path.join(MEDIA_ROOT, AVATARS_PATH, 'None'))
#
#     def setUp(self):
#         super().setUp()
#         user = User.objects.get(username='test_user')  # Получение пользователя из фикстуры
#         self.client.force_authenticate(user=user)
#
#     def test_profile_urlname(self):
#         """
#         Проверка доступности профиля пользователя по urlname
#         """
#         # self.client.force_login(user=self.test_user)
#         # self.client.login(username='test_user', password='secret_password')
#         response = self.client.get(reverse('profile'))
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_profile_update_urlname(self):
#         """
#         Проверка доступности профиля пользователя по urlname
#         """
#         # self.client.force_login(user=self.test_user)
#         self.client.login(username='test_user', password='secret_password')
#         response = self.client.post(reverse('profile'), data=self.update_data_profile)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_update_password_urlname(self):
#         """
#         Проверка доступности URL для обновления пароля по urlname
#         """
#         # self.client.force_login(user=self.test_user)
#         self.client.login(username='test_user', password='secret_password')
#         response = self.client.post(reverse('update-password'), data=self.update_data_password)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.delete_test_avatar()  # Удаляем загруженный аватар
