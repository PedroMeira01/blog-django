# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.user_views import UserViewSet
from .views.post_views import PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]