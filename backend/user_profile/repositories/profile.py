from django.contrib.auth.models import User

from backend.user_profile.models import Profile


class ProfileRepository:
    """
    CRUD-операции над профилем пользователя
    """

    @classmethod
    def create(cls, user: User) -> Profile:
        """
        Создание профиля пользователя
        :param user: пользователь
        :return: профиль пользователя
        """
        profile = Profile.objects.create(user=user)

        return profile

    @classmethod
    def get(cls, user: User) -> Profile:
        """
        Возврат профиль пользователя из БД
        :param user: пользователь
        :return: профиль пользователя
        """
        profile = Profile.objects.get(user=user)

        return profile
