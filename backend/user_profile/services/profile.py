from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from backend.user_profile.repositories.profile import ProfileRepository
from backend.user_profile.serializers.profile import ProfileSerializer


class ProfileService:

    @classmethod
    def get(cls, user: User) -> ProfileSerializer | None:
        """
        Возврат профиля пользователя
        :param user: объект текущего пользователя
        :return: профайл либо None
        """

        try:
            profile = ProfileRepository.get(user=user)
            profile_data = ProfileSerializer(profile)

        except ObjectDoesNotExist:
            profile_data = None

        return profile_data
