from rest_framework import serializers
from recipes.models import Recipe, CookingGuide, CookingGuide, Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class CookingGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingGuide
        fields = "__all__"
