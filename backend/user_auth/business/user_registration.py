import logging

from django.contrib.auth.models import User

from backend.user_profile.repositories.profile import ProfileRepository

logger = logging.getLogger(__name__)


class RegistrationUserBusiness:
    """
    Бизнес-логика приложения, отвечающая за создание (регистрацию) пользователя и профиля
    """

    @classmethod
    def __create_user(cls, data: dict) -> User:
        """
        Создание пользователя
        :param data: данные нового пользователя
        :return: объект нового пользователя
        """

        user = User(username=data['username'])
        user.set_password(data['password'])
        user.save()

        return user

    @classmethod
    def registration(cls, data: dict) -> User:
        """
        Создание нового пользователя и профиля
        :param data: данные нового пользователя
        :return: объект нового пользователя
        """

        full_name = data['name']
        count = full_name.count(' ')

        new_user = cls.__create_user(data=data)
        user_profile = ProfileRepository.create(user=new_user)

        if count == 0:
            new_user.first_name = full_name

        else:
            # Сохранение имени и фамилии в модель User, отчества в модель Profile
            full_name_list = full_name.split(' ')
            new_user.first_name = full_name_list[1]
            new_user.last_name = full_name_list[0]

            if len(full_name_list) > 2:
                user_profile.patronymic = full_name_list[2]

        new_user.save()
        user_profile.save()

        return new_user
