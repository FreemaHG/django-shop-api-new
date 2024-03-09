from typing import Dict

from backend.user_profile.models import Profile


class ProfileUpdateBusiness:
    """
    Бизнес-логика приложения, связанная с обновлением профайлом
    """

    @classmethod
    def __update_email(cls, profile: Profile, email: str) -> Profile:
        """
        Обновление email пользователя в профиле
        :param profile: профиль пользователя
        :param email: новый email
        :return: обновленный профиль
        """
        profile.user.email = email

        return profile

    @classmethod
    def __update_phone(cls, profile: Profile, phone: str) -> Profile:
        """
        Обновление номера телефона пользователя в профиле
        :param profile: профиль пользователя
        :param phone: новый номер телефона
        :return: обновленный профиль
        """
        profile.phone = phone

        return profile

    @classmethod
    def __update_full_name(cls, profile: Profile, full_name: str) -> Profile:
        """
        Обновление ФИО пользователя
        :param profile: профиль пользователя
        :param full_name: новое ФИО
        :return: обновленный профиль
        """
        profile.user.last_name = full_name[0]
        profile.user.first_name = ''

        profile.patronymic = None

        if len(full_name) > 1:
            profile.user.first_name = full_name[1]

        if len(full_name) > 2:
            profile.patronymic = full_name[2]

        return profile

    @classmethod
    def update(cls, profile: Profile, data: Dict) -> Profile:
        """
        Обновление профиля и данных пользователя
        :param profile: профиль пользователя
        :param data: новые данные
        :return: обновленные профиль
        """

        full_name = data['fullName'].split(" ")

        profile = cls.__update_full_name(profile=profile, full_name=full_name)
        profile = cls.__update_email(profile=profile, email=data['email'])
        profile = cls.__update_phone(profile=profile, phone=data['phone'])

        profile.user.save()
        profile.save()

        return profile
