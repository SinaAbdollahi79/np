from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter


app_name = "api-v1"

router = DefaultRouter()
router.register('test',views.PostModelView , basename='post')
router.register('category',views.CategoryViewSet , basename='category')
urlpatterns = router.urls



'''urlpatterns = [
    
    path("test/", views.PostList.as_view(), name='post-test'),
    path("test/<int:pk>/", views.SingelPost.as_view(), name='post-deteil'),
]'''
