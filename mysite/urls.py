from . import views
from django.urls import path,include
from django.contrib import admin


"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = "mysite"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('mysite.api.v1.urls')),
    path("xxx/", views.PostTest.as_view(), name='post-test'),
]
