import logging

from django.contrib.auth import login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from backend.serializers import ResponseInvalidDataSerializer
from backend.user_auth.serializers import LoginSerializer, RegisterSerializer
from backend.user_auth.services.login import LoginService
from backend.user_auth.services.registration import RegistrationService
from backend.user_auth.utils import reading_data_from_request

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    tags=['auth'],
    method='post',
    request_body=RegisterSerializer,
    responses={
        201: 'Пользователь успешно зарегистрирован',
        400: ResponseInvalidDataSerializer
    },
)
@api_view(['POST'])
@permission_classes([AllowAny])  # Разрешено любому пользователю
def registration(request):
    """
    Регистрация пользователя
    """

    data = reading_data_from_request(raw_data=request.data)
    authenticated_user = RegistrationService.registration(data=data)
    logging.info('Пользователь успешно зарегистрирован')

    login(request, authenticated_user)  # Авторизация нового пользователя

    return Response(status=status.HTTP_201_CREATED)


@swagger_auto_schema(
    tags=['auth'],
    method='post',
    request_body=LoginSerializer,
    responses={
        200: 'Пользователь авторизован',
        400: ResponseInvalidDataSerializer
    },
)
@api_view(['POST'])
@permission_classes([AllowAny])  # Разрешено любому пользователю
def user_login(request):
    """
    Авторизация пользователя
    """

    data = reading_data_from_request(raw_data=request.data)

    authenticated_user = LoginService.login(data=data)
    login(request, authenticated_user)
    logging.info('Пользователь успешно авторизован')

    return Response(status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=['auth'],
    method='post',
    responses={
        200: 'Пользователь вышел из учетной записи',
        403: 'The user is not logged in',
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Разрешено только аутентифицированным пользователям
def user_logout(request):
    """
    Выход из учетной записи пользователя
    """

    logout(request)
    logging.info('Пользователь вышел из учетной записи')

    return Response(status=status.HTTP_200_OK)
