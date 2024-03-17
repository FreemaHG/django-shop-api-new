import logging

from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from backend.serializers import ResponseInvalidDataSerializer
from backend.user_profile.serializers.password import PasswordSerializer
from backend.user_profile.services.password import PasswordService

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    tags=['profile'],
    methods=['post'],
    request_body=PasswordSerializer,
    responses={
        200: 'Пароль успешно обновлен',
        400: ResponseInvalidDataSerializer
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Разрешено только аутентифицированным пользователям
def update_password(request):
    """
    Обновление пароля от личного кабинета пользователя
    """

    updated_user = PasswordService.update(user=request.user, data=request.data)
    login(request=request, user=updated_user)

    return Response(status=status.HTTP_200_OK)
