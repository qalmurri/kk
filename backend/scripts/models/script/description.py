from django.db import models
from scripts.models.base import TimeStampedModel
from .script import Script

class SectionDescription(TimeStampedModel):
    '''common: pilihan section untuk model Description'''
    name = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "sectiondescription"
        verbose_name = "SectionDescription"
        verbose_name_plural = "SectionDescriptions"

class Description(TimeStampedModel):
    '''pivot: relasi section & script'''
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_Description"
    )
    sectiondescription = models.ForeignKey(
        SectionDescription,
        on_delete=models.CASCADE,
        related_name="descriptionpart_Description"
    )
    class Meta:
        db_table = "description"
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"

class TextDescription(TimeStampedModel):
    '''content: (many to one) untuk model Description, berisi tentang text'''
    description = models.ForeignKey(
        Description,
        on_delete=models.CASCADE,
        related_name="description_Text"
    )
    text = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "textdescription"
        verbose_name = "TextDescription"
        verbose_name_plural = "TextDescriptions"