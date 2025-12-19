from django.db import models
from scripts.models.scripts import Scripts
from scripts.models.timestamped import TimeStampedModel
from scripts.models.part import Part

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