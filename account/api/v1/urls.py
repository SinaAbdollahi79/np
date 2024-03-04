from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

app_name = "api-v1"


urlpatterns = [
    # regester
    path("registration/", views.RegistrationApiViews.as_view(), name="registration"),
    # change password
    path(
        "change_password/",
        views.ChangePasswordApiViews.as_view(),
        name="change_password",
    ),
    # token login and logout
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    # jwt
    path(
        "jwt/creat/",
        views.CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
]
