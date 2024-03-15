from rest_framework import authentication
from inventory.models import Ingredient, Ingredient, Ingredient
from .serializers import (
    IngredientSerializer,
    IngredientSerializer,
    IngredientSerializer,
)
from rest_framework import viewsets


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ingredient.objects.all()
