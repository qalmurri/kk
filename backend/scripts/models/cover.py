from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class CoverBook(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
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