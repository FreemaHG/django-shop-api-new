from rest_framework import serializers


class PasswordSerializer(serializers.Serializer):
    """
    Схема для обновления пароля
    """

    password = serializers.CharField()
    passwordReply = serializers.CharField()

    class Meta:
        fields = ['password', 'passwordReply']

    def validate(self, data):
        """
        Проверка, что пароли совпадают
        """

        if data['password'] != data['passwordReply']:
            raise serializers.ValidationError('Пароли не совпадают')

        return data
