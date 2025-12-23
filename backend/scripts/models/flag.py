from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class Part(TimeStampedModel):
    name = models.CharField(
        max_length=10,
    )

class Flag(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Flag"
    )
    is_active = models.BooleanField(
        default=False
    )
    part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
        related_name="part_Flag"
    )