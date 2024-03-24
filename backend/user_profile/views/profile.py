import logging

from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from backend.serializers import (
    ResponseInvalidDataSerializer,
    ResponseNotFoundSerializer,
)
from backend.user_profile.serializers.profile import (
    ProfileInSerializer,
    ProfileOutSerializer,
)
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
            404: ResponseNotFoundSerializer
        }
    )
    def get(self, request):
        """
        Вывод данных профиля текущего пользователя
        """

        profile_data = ProfileService.get(user=request.user)

        return JsonResponse(profile_data)  # Преобразуем и отправляем JSON

    @swagger_auto_schema(
        tags=['profile'],
        request_body=ProfileInSerializer,
        responses={
            200: ProfileOutSerializer,
            404: ResponseNotFoundSerializer,
            400: ResponseInvalidDataSerializer
        },
    )
    def post(self, request):
        """
        Обновление данных профиля текущего пользователя
        """

        updated_data = ProfileService.update(user=request.user, data=request.data)

        return JsonResponse(updated_data)  # Преобразуем и отправляем JSON
