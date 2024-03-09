import logging
from typing import Dict

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from backend.user_profile.serializers.password import PasswordSerializer


logger = logging.getLogger(__name__)


class PasswordService:

    @classmethod
    def update(cls, user: User, data: Dict) -> User | bool:
        """
        Обновление пароля пользователя
        :param user: объект текущего пользователя
        :param data: новые данные
        :return: обновленный пользователь
        """

        serializer = PasswordSerializer(data=data)

        if serializer.is_valid():
            user.set_password(serializer.validated_data["password"])  # Обновляем пароль
            user.save()

            # Аутентификация и авторизация пользователя
            user = authenticate(
                username=user.username,
                password=serializer.validated_data["password"]
            )

            return user

        else:
            logging.error(f"Невалидные данные: {serializer.errors}")

            return False
