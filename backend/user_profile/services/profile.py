import logging
from typing import Dict, Union

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from backend.user_profile.business.update_profile import ProfileUpdateBusiness
from backend.user_profile.repositories.profile import ProfileRepository
from backend.user_profile.serializers.profile import ProfileOutSerializer, ProfileInSerializer


logger = logging.getLogger(__name__)


class ProfileService:

    @classmethod
    def get(cls, user: User) -> ProfileOutSerializer | None:
        """
        Возврат профиля пользователя
        :param user: объект текущего пользователя
        :return: профайл либо None
        """

        try:
            profile = ProfileRepository.get(user=user)
            profile_data = ProfileOutSerializer(profile)

        except ObjectDoesNotExist:
            profile_data = None

        return profile_data

    @classmethod
    def update(cls, user: User, data: Dict) -> Union[Dict, None, bool]:
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
            serializer = ProfileOutSerializer(updated_profile)  # Сериализация данных

            return serializer.data

        else:
            logging.error(f"Невалидные данные: {serializer.errors}")
            return False
