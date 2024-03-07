from django.contrib.auth.models import User

from backend.user_profile.models import Profile


class ProfileRepository:
    """
    CRUD-операции над профилем пользователя
    """

    @classmethod
    def create(cls):
        pass

    @classmethod
    def get(cls, user: User) -> Profile:
        """
        Возврат профиль пользователя из БД
        :param user: пользователь
        :return: профайл пользователя
        """
        return Profile.objects.get(user=user)

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls):
        pass
