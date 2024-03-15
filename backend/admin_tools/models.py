from django.conf import settings
from django.db import models


class Report(models.Model):
    "Generated Model"
    issue_type = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    reported_by = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="report_reported_by",
    )


# Create your models here.
