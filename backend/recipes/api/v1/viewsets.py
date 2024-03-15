from rest_framework import authentication
from recipes.models import (
    Recipe,
    CookingGuide,
    CookingGuide,
    Recipe,
    CookingGuide,
    Recipe,
)
from .serializers import (
    RecipeSerializer,
    CookingGuideSerializer,
    CookingGuideSerializer,
    RecipeSerializer,
    CookingGuideSerializer,
    RecipeSerializer,
)
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Recipe.objects.all()


class CookingGuideViewSet(viewsets.ModelViewSet):
    serializer_class = CookingGuideSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CookingGuide.objects.all()
