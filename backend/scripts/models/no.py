from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class No(TimeStampedModel):
    no = models.CharField(
        max_length=255
    )
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_No",
        null=True,
        blank=True
    )

