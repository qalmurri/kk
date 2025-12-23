from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class DescriptionPart(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )

class Description(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Description"
    )
    descriptionpart = models.ForeignKey(
        DescriptionPart,
        on_delete=models.CASCADE,
        related_name="descriptionpart_Description"
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