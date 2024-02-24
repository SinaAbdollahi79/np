from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = "api-v1"


urlpatterns = [

    path("registration/", views.RegistrationApiViews.as_view(), name='registration'),


]
