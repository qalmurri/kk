from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.institute import Institute

class Orderer(TimeStampedModel): #MigrateDone
    name = models.CharField(
        max_length=255
    )
    no = models.IntegerField(
        null=True,
        blank=True
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_Orderer",
        null=True,
        blank=True
    )