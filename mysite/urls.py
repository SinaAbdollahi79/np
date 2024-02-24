from . import views
from django.urls import path,include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="First API",
      default_version='v1',
      description="First api  description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = "mysite"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('mysite.api.v1.urls')),
    path("api/v1/account/", include('account.urls')),
    path("xxx/", views.PostTest.as_view(), name='post-test'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-docs/',include_docs_urls(title='Superbook API')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger/output.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]
