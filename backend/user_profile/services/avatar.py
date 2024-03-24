import logging

from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

from backend.exceptions import NotFoundResponseException
from backend.user_profile.repositories.profile import ProfileRepository
from backend.user_profile.serializers.avatar import ImageSerializer

logger = logging.getLogger(__name__)


class AvatarService:

    @classmethod
    def update(cls, user: User, avatar: str) -> dict:
        """
        Обновление аватара пользователя
        :param user: объект текущего пользователя
        :param avatar: новая аватарка
        :return: словарь с обновленными данными
        """
        try:
            profile = ProfileRepository.get(user=user)

        except ObjectDoesNotExist:
            logging.error('Профиль пользователя не найден')
            raise NotFoundResponseException(detail='Профиль пользователя не найден')

        profile.avatar = avatar
        profile.save()

        cache.delete('profile')
        logger.info('Кэш профиля очищен')

        serializer = ImageSerializer(
            data={
                'src': '/' + str(profile.avatar),
                'alt': profile.__str__()
            }
        )

        return serializer.initial_data
