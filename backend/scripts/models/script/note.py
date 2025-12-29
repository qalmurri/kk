from django.db import models
from scripts.models.base import TimeStampedModel
from .script import Script

class SectionNote(TimeStampedModel):
    '''common: pilihan section untuk model Note'''
    name = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "sectionnote"
        verbose_name = "SectionNote"
        verbose_name_plural = "SectionNotes"

class Note(TimeStampedModel):
    '''pivot: relasi section & script'''
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    sectionnote = models.ForeignKey(
        SectionNote,
        on_delete=models.CASCADE,
        related_name="notepart_Note"
    )
    class Meta:
        db_table = "note"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

class TextNote(TimeStampedModel):
    '''content: (many to one) untuk model Note, berisi tentang text'''
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="note_Content"
    )
    text = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "textnote"
        verbose_name = "TextNote"
        verbose_name_plural = "TextNotes"