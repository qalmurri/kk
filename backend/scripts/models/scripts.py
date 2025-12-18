from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.institute import Institute
from scripts.models.size import Size

class Scripts(TimeStampedModel): #MigrateDone
    is_active = models.BooleanField(default=True)
    title = models.CharField(
        max_length=255
    )
    alias = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    entry_date = models.DateField(
        null=True,
        blank=True
    )
    finish_date = models.DateField(
        null=True,
        blank=True
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_Scripts",
        null=True,
        blank=True
    )

    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="size_Scripts",
        null=True,
        blank=True
    )

