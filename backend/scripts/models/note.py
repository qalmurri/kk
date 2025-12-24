from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.script import Script

class NotePart(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "notepart"
        verbose_name = "NotePart"
        verbose_name_plural = "NoteParts"

class Note(TimeStampedModel):
    scripts = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    notepart = models.ForeignKey(
        NotePart,
        on_delete=models.CASCADE,
        related_name="notepart_Note"
    )
    class Meta:
        db_table = "note"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

class Content(TimeStampedModel):
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="note_Content"
    )
    content = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "content"
        verbose_name = "Content"
        verbose_name_plural = "Contents"
