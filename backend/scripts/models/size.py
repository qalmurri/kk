from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Size(TimeStampedModel): #MigrateDone
    name = models.CharField(
        max_length=255
    )
