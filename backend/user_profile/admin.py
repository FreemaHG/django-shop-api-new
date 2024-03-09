import logging

from django.contrib import admin

from backend.user_profile.models import Profile


logger = logging.getLogger(__name__)


@admin.action(description="Мягкое удаление")
def deleted_records(adminmodel, request, queryset):
    """
    Мягкое удаление записей (смена статуса)
    """
    queryset.update(deleted=True)

@admin.action(description="Восстановить записи")
def restore_records(adminmodel, request, queryset):
    """
    Восстановить записи, отключенные ч/з мягкое удаление (смена статуса)
    """
    queryset.update(deleted=False)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Админ-панель для профайла пользователей
    """

    list_display = ["id", "full_name", "email", "phone", "deleted"]
    list_display_links = ("full_name",)
    list_editable = ("deleted",)

    # Мягкое удаление/восстановление записей
    actions = (
        deleted_records,
        restore_records,
    )

    @admin.display(description='ФИО')
    def full_name(self, object):
        return object.__str__()

    @admin.display(description='Email')
    def email(self, object):
        return object.user.email

    # Детальная страница профайла
    readonly_fields = ['username', 'first_name', 'last_name', 'email']

    fieldsets = (
        (
            "Данные аккаунта", {
                "fields": ("username", "first_name", "last_name", "email"),
                "description": "Основные данные пользователя",
            }
        ),
        (
            "Данные профиля", {
                "fields": ("patronymic", "phone", "avatar", "deleted"),
                "description": "Дополнительные данные пользователя",
            },
        ),
    )

    @admin.display(description='Никнейм')
    def username(self, obj):
        return obj.user.username

    @admin.display(description='Имя')
    def first_name(self, obj):
        return obj.user.first_name

    @admin.display(description='Фамилия')
    def last_name(self, obj):
        return obj.user.last_name

    @admin.display(description='Email')
    def email(self, obj):
        return obj.user.email
