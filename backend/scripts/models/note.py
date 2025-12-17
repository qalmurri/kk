from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class Note(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    content = models.CharField(
        max_length=255
    )
    label = models.IntegerField()