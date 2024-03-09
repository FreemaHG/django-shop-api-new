import logging

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.user_profile.serializers.profile import ProfileOutSerializer, ProfileInSerializer
from backend.user_profile.services.profile import ProfileService


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
            200: ProfileOutSerializer,
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

    @swagger_auto_schema(
        tags=["profile"],
        request_body=ProfileInSerializer,
        responses={
            200: ProfileOutSerializer,
            404: "No data found"
        },
    )
    def post(self, request):
        """
        Обновление профайла пользователя
        """

        updated_data = ProfileService.update(user=request.user, data=request.data)

        if updated_data is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        elif updated_data is False:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        logger.info("Данные профайла обновлены")
        return JsonResponse(updated_data)  # Преобразуем и отправляем JSON
