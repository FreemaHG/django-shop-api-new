import logging

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from backend.exceptions import InvalidDataResponseException
from backend.user_auth.serializers import LoginSerializer

logger = logging.getLogger(__name__)


class LoginService:

    @classmethod
    def login(cls, data: dict) -> User:
        """
        Авторизация пользователя
        :param data: данные для регистрации
        :return: объект аутентифицированного пользователя
        """

        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            # Аутентификация
            authenticated_user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )

            if authenticated_user is not None:
                # TODO Реализовать позже слияние корзин гостя и пользователя в БД!!!
                # BasketService.merger(request=request, user=user)
                return authenticated_user

            else:
                logging.error('Логин или пароль не совпадают')
                raise InvalidDataResponseException(detail='Логин или пароль не совпадают')

        else:
            logging.error(f'Невалидные данные: {serializer.errors}')
            raise InvalidDataResponseException(detail=serializer.errors)
