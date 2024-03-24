from django.urls import path

from backend.user_profile.views.profile import ProfileView
from backend.user_profile.views.update_avatar import update_avatar
from backend.user_profile.views.update_password import update_password

urlpatterns = [
    path('password/', update_password, name='update-password'),
    path('avatar/', update_avatar, name='update-avatar'),
    path('', ProfileView.as_view(), name='profile'),
]
