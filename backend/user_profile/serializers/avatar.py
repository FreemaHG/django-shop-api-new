from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    """
    Схема для изображений
    """

    src = serializers.CharField()
    alt = serializers.CharField()

    class Meta:
        fields = '__all__'
