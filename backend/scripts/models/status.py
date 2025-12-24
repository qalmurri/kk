from django.db import models
from scripts.models.base import TimeStampedModel
from scripts.models.script import Script

class SectionStatus(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )
    class Meta:
        db_table = "sectionstatus"
        verbose_name = "SectionStatus"
        verbose_name_plural = "SectionStatuss"

class LabelStatus(TimeStampedModel):
    name = models.CharField(
        max_length=10,
    )
    class Meta:
        db_table = "labelstatus"
        verbose_name = "LabelStatus"
        verbose_name_plural = "LabelStatuss"

class Status(TimeStampedModel):
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_Status"
    )
    labelstatus = models.ForeignKey(
        LabelStatus,
        on_delete=models.CASCADE,
        related_name="label_Status"
    )
    sectionstatus = models.ForeignKey(
        SectionStatus,
        on_delete=models.CASCADE,
        related_name="code_Status"
    )
    class Meta:
        db_table = "status"
        verbose_name = "Status"
        verbose_name_plural = "Statuss"