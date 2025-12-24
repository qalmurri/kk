from django.db import models
from scripts.models.timestamped import TimeStampedModel

class Size(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "size"
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

class Institute(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "institute"
        verbose_name = "Institute"
        verbose_name_plural = "Institutes"