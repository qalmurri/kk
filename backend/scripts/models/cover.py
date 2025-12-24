from django.db import models
from scripts.models.base import TimeStampedModel
from scripts.models.script import Script

class CoverBook(TimeStampedModel):
    scripts = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_Cover"
    )
    thumbnail = models.CharField(
        max_length=255
    )
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    x_axis = models.IntegerField(
        default=0
    )
    y_axis = models.IntegerField(
        default=0
    )
    class Meta:
        db_table = "coverbook"
        verbose_name = "CoverBook"
        verbose_name_plural = "CoverBooks"