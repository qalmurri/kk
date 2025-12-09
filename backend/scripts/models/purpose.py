from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Purpose(TimeStampedModel): #MigrateDone
    code = models.IntegerField(db_index=True)
    purpose = models.CharField(
        max_length=255
    )
    class Meta:
        unique_together = (
            'code',
            'purpose'
        )