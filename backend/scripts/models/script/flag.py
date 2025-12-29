from django.db import models
from scripts.models.base import TimeStampedModel
from .script import Script

class SectionFlag(TimeStampedModel):
    name = models.CharField(
        max_length=10,
    )
    class Meta:
        db_table = "part"
        verbose_name = "Part"
        verbose_name_plural = "Parts"

class Flag(TimeStampedModel):
    scripts = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_Flag"
    )
    is_active = models.BooleanField(
        default=False
    )
    sectionflag = models.ForeignKey(
        SectionFlag,
        on_delete=models.CASCADE,
        related_name="part_Flag"
    )
    class Meta:
        db_table = "flag"
        verbose_name = "Flag"
        verbose_name_plural = "Flags"