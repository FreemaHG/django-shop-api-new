from django.contrib.auth.models import User
from django.db import models
from phone_field.models import PhoneField

from backend.config import STATUS_CHOICES
from backend.user_profile.utils.save_file import avatar_path


class Profile(models.Model):
    """
    Профайл пользователя
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name='отчество')
    phone = PhoneField(blank=True, null=True, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to=avatar_path, blank=True, null=True, verbose_name='аватар')
    deleted = models.BooleanField(choices=STATUS_CHOICES, default=False, verbose_name='статус')

    class Meta:
        db_table = 'profile'
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'

    def __str__(self):
        last_name = self.user.last_name
        first_name = self.user.first_name
        patronymic = self.patronymic

        if last_name or first_name or patronymic:
            return f'{last_name} {first_name} {patronymic}'.replace('None', '')

        return self.user.username
