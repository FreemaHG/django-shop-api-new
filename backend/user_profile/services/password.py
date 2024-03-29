import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from backend.exceptions import InvalidDataResponseException
from backend.user_profile.serializers.password import PasswordSerializer

logger = logging.getLogger(__name__)


class PasswordService:

    @classmethod
    def update(cls, user: User, data: dict) -> User:
        """
        Обновление пароля пользователя
        :param user: объект текущего пользователя
        :param data: новые данные
        :return: обновленный пользователь
        """

        serializer = PasswordSerializer(data=data)

        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])  # Обновляем пароль
            user.save()

            # Аутентификация и авторизация пользователя
            user = authenticate(
                username=user.username,
                password=serializer.validated_data['password']
            )

            logger.info('пароль обновлен')
            return user

        else:
            logging.error(f'Невалидные данные: {serializer.errors}')
            raise InvalidDataResponseException(detail=serializer.errors)
