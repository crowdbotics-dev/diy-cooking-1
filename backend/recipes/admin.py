from django.contrib import admin
from .models import CookingGuide, Recipe

admin.site.register(Recipe)
admin.site.register(CookingGuide)

# Register your models here.
