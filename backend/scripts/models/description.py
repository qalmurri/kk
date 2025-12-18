from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.label import Label

class Description(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Description"
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name="label_Description"
    )

class Text(TimeStampedModel):
    description = models.ForeignKey(
        Description,
        on_delete=models.CASCADE,
        related_name="description_Text"
    )
    text = models.CharField(
        max_length=255
    )