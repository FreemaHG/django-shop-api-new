import logging

from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

from backend.user_profile.business.update_profile import ProfileUpdateBusiness
from backend.user_profile.repositories.profile import ProfileRepository
from backend.user_profile.serializers.profile import (
    ProfileInSerializer,
    ProfileOutSerializer,
)

logger = logging.getLogger(__name__)


class ProfileService:

    @classmethod
    def get(cls, user: User) -> dict | None:
        """
        Возврат профиля пользователя
        :param user: объект текущего пользователя
        :return: профайл либо None
        """

        cached_data = cache.get('profile')

        if cached_data:
            logger.debug('Данные из кэша')
            return cached_data

        else:
            try:
                profile = ProfileRepository.get(user=user)

            except ObjectDoesNotExist:
                logger.error('Профиль пользователя не найден')
                return None

            profile_data = ProfileOutSerializer(profile)
            cache.set('profile', profile_data.data)

            return profile_data.data

    @classmethod
    def update(cls, user: User, data: dict) -> dict | None | bool:
        """
        Обновление профиля пользователя
        :param user: объект текущего пользователя
        :param data: новые данные
        :return: обновленные данные профиля
        """

        serializer = ProfileInSerializer(data=data)

        if serializer.is_valid():
            try:
                profile = ProfileRepository.get(user=user)

            except ObjectDoesNotExist:
                logger.error('Профиль пользователя не найден')
                return None

            updated_profile = ProfileUpdateBusiness.update(profile=profile, data=serializer.validated_data)
            logger.info('Данные профайла обновлены')

            serializer = ProfileOutSerializer(updated_profile)  # Сериализация данных

            cache.delete('profile')
            logger.info('Кэш профиля очищен')

            return serializer.data

        else:
            logging.error(f'Невалидные данные: {serializer.errors}')
            return False
