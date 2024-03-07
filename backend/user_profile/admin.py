from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from backend.user_profile.models import Profile


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

    fieldsets = (("Основное", {"fields": ("user", "patronymic", "phone", "avatar", "deleted")}),)

    def full_name(self, object):
        return object.__str__()

    full_name.short_description = "ФИО"

    def email(self, object):
        return object.user.email

    email.short_description = "Email"
