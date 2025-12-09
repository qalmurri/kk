from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Institute(TimeStampedModel): #MigrateDone
    institute = models.CharField(
        max_length=255
    )