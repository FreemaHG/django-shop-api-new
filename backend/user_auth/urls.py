from django.urls import path

from backend.user_auth.views import registration

urlpatterns = [
    path('-up/', registration, name='sign-up'),
    # path("-in/", login, name="sign-in"),
    # path("-out/", logout, name="sign-out"),
]
