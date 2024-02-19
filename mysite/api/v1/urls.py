from . import views
from django.urls import path, include


app_name = "api-v1"

urlpatterns = [
    
    path("test/", views.post_test, name='post-test'),
]
