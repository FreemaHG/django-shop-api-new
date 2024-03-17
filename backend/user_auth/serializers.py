from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    """
    Схема для авторизации пользователя
    """

    username = serializers.CharField(max_length=300, required=True, label='Логин или Email')
    password = serializers.CharField(
        required=True,
        write_only=True,
        label='Пароль',
        style={'input_type': 'password'},
        trim_whitespace=False,
    )


class RegisterSerializer(LoginSerializer):
    """
    Схема для регистрации пользователя
    """

    name = serializers.CharField(max_length=300, required=True, label='ФИО')
