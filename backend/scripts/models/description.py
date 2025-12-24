from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.script import Script

# Common
class SectionDescription(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )
    class Meta:
        db_table = "sectiondescription"
        verbose_name = "SectionDescription"
        verbose_name_plural = "SectionDescriptions"

# Pivot
class Description(TimeStampedModel):
    scripts = models.ForeignKey(
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

# Content
class TextDescription(TimeStampedModel):
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