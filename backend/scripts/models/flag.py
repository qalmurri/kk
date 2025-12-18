from django.db import models
from scripts.models.scripts import Scripts
from scripts.models.timestamped import TimeStampedModel
from scripts.models.label import Label

class Flag(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Flag"
    )
    is_active = models.BooleanField(
        default=False
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name="label_Flag"
    )