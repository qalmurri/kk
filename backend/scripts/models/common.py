from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Size(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )

class Institute(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )