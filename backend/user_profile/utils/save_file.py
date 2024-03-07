import logging
import os


logger = logging.getLogger(__name__)

_AVATARS_PATH = os.path.join('images', 'avatars')


def avatar_path(instance, filename: str) -> str:
    """
    Генерация директории для сохранения аватара пользователя
    :param instance: профайл пользователя
    :param filename: название файла
    :return: директория для сохранения аватара
    """

    return os.path.join(
        'user_profile', 'static', _AVATARS_PATH, f'{instance.id}', filename
    )
