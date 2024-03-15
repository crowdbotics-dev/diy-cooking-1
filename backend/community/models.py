from django.conf import settings
from django.db import models


class CommunityPost(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=255,
    )
    content = models.TextField()
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="communitypost_author",
    )


# Create your models here.
