from rest_framework import serializers


class ResponseNotFoundSerializer(serializers.Serializer):
    """
    Схема для возврата ответа, если запись не найдена
    """

    detail = serializers.CharField(default='Запись не найдена')


class ResponseInvalidDataSerializer(serializers.Serializer):
    """
    Схема для возврата ответа при передаче невалидных данных
    """

    detail = serializers.CharField(default='Переданы невалидные данные')
