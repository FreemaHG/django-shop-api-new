import logging

from typing import Dict
from rest_framework import serializers

from backend.user_profile.models import Profile


logger = logging.getLogger(__name__)


class ProfileSerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных профайла пользователя
    """

    fullName = serializers.SerializerMethodField("full_name")
    email = serializers.SerializerMethodField("get_email")
    phone = serializers.CharField()
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
