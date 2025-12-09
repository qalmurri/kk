from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Size(TimeStampedModel): #MigrateDone
    size = models.CharField(
        max_length=255
    )
