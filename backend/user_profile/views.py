import logging

from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.user_profile.models import Profile
from backend.user_profile.serializers.profile import ProfileSerializer

# from src.api_user.models import Profile
# from src.api_user.models import ImageForAvatar
# from src.api_user.serializers.password import PasswordSerializer
# from src.api_shop.serializers.image import ImageSerializer


logger = logging.getLogger(__name__)


# @swagger_auto_schema(
#     tags=["profile"],
#     methods=["post"],
#     responses={200: ImageSerializer, 400: "Error updating avatar"},
# )
# @api_view(["POST"])
# @permission_classes(
#     [IsAuthenticated]
# )  # Разрешено только аутентифицированным пользователям
# def update_avatar(request):
#     """
#     Обновление аватара
#     """
#     logging.debug("Обновление аватара")
#
#     avatar = request.FILES["avatar"]
#     profile = Profile.objects.get(user=request.user)
#
#     ImageForAvatar.objects.filter(profile=profile).delete()  # Удаляем старый аватар
#
#     # Создаем новый аватар
#     image = ImageForAvatar(path="", alt="Аватар", profile=profile)
#     image.path.save(avatar.name, avatar)
#
#     profile.avatar = image
#     profile.save()
#     logger.info("Аватарка обновлена")
#
#     serializer = ImageSerializer(image)  # Сериализация данных
#
#     return JsonResponse(serializer.data)  # Преобразуем и отправляем JSON


# @swagger_auto_schema(
#     tags=["profile"],
#     methods=["post"],
#     request_body=PasswordSerializer,
#     responses={200: "password updated", 400: "Invalid data"},
# )
# @api_view(["POST"])
# @permission_classes(
#     [IsAuthenticated]
# )  # Разрешено только аутентифицированным пользователям
# def update_password(request):
#     """
#     Обновление пароля
#     """
#     logging.debug("Обновление пароля")
#     serializer = PasswordSerializer(data=request.data)
#
#     if serializer.is_valid():
#         user = request.user
#         user.set_password(serializer.validated_data["password"])  # Обновляем пароль
#         user.save()
#         logger.info("пароль обновлен")
#
#         # Аутентификация и авторизация пользователя
#         user = authenticate(
#             username=user.username, password=serializer.validated_data["password"]
#         )
#         login(request, user)
#
#         return Response(status=status.HTTP_200_OK)
#
#     else:
#         logging.error(f"Невалидные данные: {serializer.errors}")
#         return Response(status=status.HTTP_400_BAD_REQUEST)