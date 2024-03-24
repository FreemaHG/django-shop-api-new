from django.urls import path

from backend.user_auth.views import registration, user_login, user_logout

urlpatterns = [
    path('-up/', registration, name='sign-up'),
    path('-in/', user_login, name='sign-in'),
    path('-out/', user_logout, name='sign-out'),
]
