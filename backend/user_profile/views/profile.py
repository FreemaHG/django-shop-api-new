import logging

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.user_profile.serializers.profile import ProfileOutSerializer
from backend.user_profile.services.profile import ProfileService

logger = logging.getLogger(__name__)


class ProfileView(APIView):
    """
    Вывести или обновить данные профайла
    """

    # Разрешено только аутентифицированным пользователям
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['profile'],
        responses={
            200: ProfileOutSerializer,
            404: 'Профиль не найден'
        }
    )
    def get(self, request):
        """
        Вывод данных профиля текущего пользователя
        """

        profile_data = ProfileService.get(user=request.user)

        if not profile_data:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return JsonResponse(profile_data)  # Преобразуем и отправляем JSON

    @swagger_auto_schema(
        tags=['profile'],
        request_body=ProfileOutSerializer,
        responses={
            200: ProfileOutSerializer,
            404: 'Профиль не найден'
        },
    )
    def post(self, request):
        """
        Обновление данных профиля текущего пользователя
        """

        updated_data = ProfileService.update(user=request.user, data=request.data)

        if updated_data is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        elif updated_data is False:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(updated_data)  # Преобразуем и отправляем JSON