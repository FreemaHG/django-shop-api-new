from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    """
    Схема для изображений
    """

    src = serializers.SerializerMethodField('get_src')
    alt = serializers.CharField(default='Аватарка пользователя')

    def get_src(self, obj):
        if obj:
            return '/' + obj.__str__()
        return ''

    class Meta:
        fields = ['src', 'alt']
