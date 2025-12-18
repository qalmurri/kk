from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.label import Label

class Note(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name="label_Note"
    )

class Content(TimeStampedModel):
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="note_Content"
    )
    content = models.CharField(
        max_length=255
    )