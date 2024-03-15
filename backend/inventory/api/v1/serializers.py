from rest_framework import serializers
from inventory.models import Ingredient, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"
