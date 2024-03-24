from django.urls import path

from backend.user_auth.views import registration, user_login

urlpatterns = [
    path('-up/', registration, name='sign-up'),
    path('-in/', user_login, name='sign-in'),
    # path("-out/", logout, name="sign-out"),
]
