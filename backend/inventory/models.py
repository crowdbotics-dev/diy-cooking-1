from django.conf import settings
from django.db import models


class Ingredient(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    expiry_date = models.DateField(
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="ingredient_user",
    )


# Create your models here.
