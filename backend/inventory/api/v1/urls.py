from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    IngredientViewSet,
    IngredientViewSet,
    IngredientViewSet,
    IngredientViewSet,
)

router = DefaultRouter()
router.register("ingredient", IngredientViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
