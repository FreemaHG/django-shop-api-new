import json
import logging

from django.contrib.auth import login
from django.http import QueryDict
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.serializers import ResponseInvalidDataSerializer
from backend.user_auth.serializers import RegisterSerializer
from backend.user_auth.services.register import RegistrationService

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
    raw_data = request.data

    if not isinstance(raw_data, QueryDict):
        logger.debug('Передача данных с Swagger')
        data = raw_data

    else:
        logger.debug('Передача данных с фронта')
        data = list(dict(raw_data).keys())[0]  # Достаем ключ из QueryDict - словарь с данными
        data = json.loads(data)

    authenticated_user = RegistrationService.registration(data=data)
    login(request, authenticated_user)  # Авторизация нового пользователя

    return Response(status=status.HTTP_201_CREATED)


# @swagger_auto_schema(
#     tags=["auth"],
#     method="post",
#     request_body=UserLoginSerializer,
#     responses={200: "The user is authenticated", 400: "Invalid data"},
# )
# @api_view(["POST"])
# @permission_classes([AllowAny])  # Разрешено любому пользователю
# def login(request):
#     """
#     Авторизация пользователя
#     """
#     logging.debug("Авторизация пользователя")
#
#     data = json.loads(request.body)
#     serializer = UserLoginSerializer(data=data)
#
#     if serializer.is_valid(raise_exception=True):
#         user = authenticate(
#             username=data["username"], password=data["password"]
#         )  # Аутентификация
#         login(request, user)  # Авторизация нового пользователя
#         logging.info(f"Пользователь аутентифицирован")
#
#         BasketService.merger(request=request, user=user)  # Слияние корзин
#
#         return Response(None, status=status.HTTP_200_OK)
#
#     else:
#         logging.error(f"Невалидные данные: {serializer.errors}")
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @swagger_auto_schema(
#     tags=["auth"],
#     method="post",
#     responses={
#         200: "The user logged out of the account",
#         403: "The user is not logged in",
#     },
# )
# @api_view(["POST"])
# @permission_classes(
#     [IsAuthenticated]
# )  # Разрешено только аутентифицированным пользователям
# def logout(request):
#     """
#     Выход из учетной записи пользователя
#     """
#     logging.debug("Выход из учетной записи")
#     logout(request)
#
#     return Response(None, status=status.HTTP_200_OK)
