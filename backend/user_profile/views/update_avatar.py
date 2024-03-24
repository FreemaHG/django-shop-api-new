import logging

from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from backend.serializers import ResponseNotFoundSerializer
from backend.user_profile.serializers.avatar import ImageSerializer
from backend.user_profile.services.avatar import AvatarService

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    tags=['profile'],
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY)
        }
    ),
    responses={
        200: ImageSerializer,
        404: ResponseNotFoundSerializer
    },
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Разрешено только аутентифицированным пользователям
def update_avatar(request):
    """
    Обновление аватара в профиле текущего пользователя
    """

    updated_avatar = AvatarService.update(user=request.user, avatar=request.FILES['avatar'])

    return JsonResponse(updated_avatar)
