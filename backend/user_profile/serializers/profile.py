import logging

from typing import Dict
from rest_framework import serializers

from backend.user_profile.models import Profile


logger = logging.getLogger(__name__)


# TODO Перенести в другое место
class ImageSerializer(serializers.Serializer):
    """
    Схема для изображений
    """

    src = serializers.CharField()
    alt = serializers.CharField(max_length=250, default="")

    class Meta:
        fields = ["src", "alt"]


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
    avatar = serializers.SerializerMethodField("get_avatar")

    def full_name(self, obj) -> str:
        return obj.__str__()

    def get_avatar(self, obj) -> Dict:
        # Для корректной подстановки в frontend
        return {
            'src': '/' + obj.avatar.__str__(),
            'alt': obj.__str__()
        }

    def get_email(self, obj) -> str:
        return obj.user.email

    class Meta:
        model = Profile
        fields = ["fullName", "email", "phone", "avatar"]
