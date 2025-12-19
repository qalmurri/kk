from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class NotePart(models.Model):
    name = models.CharField(max_length=255)

class Note(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    notepart = models.ForeignKey(
        NotePart,
        on_delete=models.CASCADE,
        related_name="notepart_Note"
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