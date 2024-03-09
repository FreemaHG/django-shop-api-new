import logging

from rest_framework import serializers

from backend.user_profile.models import Profile
from backend.user_profile.serializers.avatar import ImageSerializer

logger = logging.getLogger(__name__)


class ProfileInSerializer(serializers.Serializer):
    """
    Схема для обновления данных профайла пользователя
    """

    fullName = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()


class ProfileOutSerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных профайла пользователя
    """

    fullName = serializers.SerializerMethodField("full_name")
    phone = serializers.CharField()
    email = serializers.SerializerMethodField("get_email")
    avatar = ImageSerializer()

    def full_name(self, obj) -> str:
        return obj.__str__()

    def get_email(self, obj) -> str:
        return obj.user.email

    class Meta:
        model = Profile
        fields = ["fullName", "email", "phone", "avatar"]
