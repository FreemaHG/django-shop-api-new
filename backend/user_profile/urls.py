from django.urls import path, include

from backend.user_profile.views.profile import ProfileView

# from src.api_user.api.auth import register_user, user_login, user_logout
# from src.api_user.api.profile import update_avatar, update_password, ProfileView


urlpatterns = [
    # path('password/', update_password, name='update-password'),
    # path('avatar/', update_avatar, name='update-profile'),
    path('', ProfileView.as_view(), name='profile'),
]