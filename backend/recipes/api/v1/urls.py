from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecipeViewSet,
    CookingGuideViewSet,
    CookingGuideViewSet,
    RecipeViewSet,
    CookingGuideViewSet,
    RecipeViewSet,
    CookingGuideViewSet,
    RecipeViewSet,
)

router = DefaultRouter()
router.register("recipe", RecipeViewSet)
router.register("cookingguide", CookingGuideViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
