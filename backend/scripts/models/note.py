from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class Note(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    label = models.IntegerField()

class Content(TimeStampedModel):
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="note_Content"
    )
    content = models.CharField(
        max_length=255
    )