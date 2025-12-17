from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Institute(TimeStampedModel): #MigrateDone
    name = models.CharField(
        max_length=255
    )