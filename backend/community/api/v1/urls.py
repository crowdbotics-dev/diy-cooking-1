from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CommunityPostViewSet,
    CommunityPostViewSet,
    CommunityPostViewSet,
    CommunityPostViewSet,
)

router = DefaultRouter()
router.register("communitypost", CommunityPostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
