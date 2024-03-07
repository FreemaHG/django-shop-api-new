import logging

from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.user_profile.models import Profile
from backend.user_profile.serializers.profile import ProfileSerializer
from backend.user_profile.services.profile import ProfileService

# from src.api_user.models import Profile
# from src.api_user.models import ImageForAvatar
# from src.api_user.serializers.password import PasswordSerializer
# from src.api_shop.serializers.image import ImageSerializer


logger = logging.getLogger(__name__)


class ProfileView(APIView):
    """
    Вывести или обновить данные профайла
    """

    # Разрешено только аутентифицированным пользователям
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["profile"],
        responses={
            200: ProfileSerializer,
            404: "No data found"
        }
    )
    def get(self, request):
        """
        Вывод профайла пользователя
        """

        profile = ProfileService.get(user=request.user)

        if not profile:
            logger.error("Профиль пользователя не найден")
            return Response(status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(profile.data)  # Преобразуем и отправляем JSON




    # @swagger_auto_schema(
    #     tags=["profile"],
    #     request_body=ProfileSerializer,
    #     responses={200: ProfileSerializer, 404: "No data found"},
    # )
    # def post(self, request, format=None):
    #     logging.debug("Обновление данных профайла")
    #
    #     serializer = ProfileSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         logger.debug(f"Данные валидны: {serializer.validated_data}")
    #         profile = Profile.objects.get(user=request.user)
    #         profile = serializer.update(profile, serializer.validated_data)
    #         serializer = ProfileSerializer(profile)  # Сериализация данных
    #
    #         logger.info("Данные профайла обновлены")
    #         return JsonResponse(serializer.data)  # Преобразуем и отправляем JSON
    #
    #     else:
    #         logging.error(f"Невалидные данные: {serializer.errors}")
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
