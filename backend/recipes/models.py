from django.conf import settings
from django.db import models


class Recipe(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=255,
    )
    cuisine = models.CharField(
        max_length=100,
    )
    difficulty_level = models.CharField(
        max_length=50,
    )
    ingredients = models.TextField()
    steps = models.TextField()
    cooking_tips = models.TextField(
        null=True,
        blank=True,
    )
    creator = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="recipe_creator",
    )


class CookingGuide(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=255,
    )
    steps = models.TextField()
    difficulty_rating = models.CharField(
        max_length=50,
    )
    preparation_time = models.CharField(
        max_length=50,
    )


# Create your models here.
