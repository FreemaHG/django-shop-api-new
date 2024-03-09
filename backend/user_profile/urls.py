from django.urls import path

from backend.user_profile.views.profile import ProfileView
from backend.user_profile.views.update_avatar import update_avatar


urlpatterns = [
    # path('password/', update_password, name='update-password'),
    path('avatar/', update_avatar, name='update-profile'),
    path('', ProfileView.as_view(), name='profile'),
]