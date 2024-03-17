import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from backend.exceptions import InvalidDataResponseException
from backend.user_auth.business.user_registration import RegistrationUserBusiness
from backend.user_auth.serializers import RegisterSerializer

logger = logging.getLogger(__name__)


class RegistrationService:
    """
    Регистрация нового пользователя
    """

    @classmethod
    def registration(cls, data: dict) -> User:
        """
        Регистрация пользователя
        :param data: данные для регистрации
        :return: объект нового пользователя
        """

        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            user = User.objects.filter(username=serializer.validated_data['username'])

            if user:
                logger.error('Пользователь с таким именем уже зарегистрирован')
                raise InvalidDataResponseException(detail='Пользователь с таким именем уже зарегистрирован')

            new_user = RegistrationUserBusiness.registration(data=serializer.validated_data)

            # Аутентификация пользователя
            authenticated_user = authenticate(
                username=new_user.username,
                password=serializer.validated_data['password']
            )

            return authenticated_user

        else:
            logger.error(f'Невалидные данные: {serializer.errors}')
            raise InvalidDataResponseException(detail=serializer.errors)
