from django.db import models
from scripts.models.base import TimeStampedModel
from scripts.models.common import (
    Institute,
    Size
)

class Script(TimeStampedModel):
    is_active = models.BooleanField(
        default=True
    )
    title = models.CharField(
        max_length=255
    )
    alias = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    entry_date = models.DateField(
        null=True,
        blank=True
    )
    finish_date = models.DateField(
        null=True,
        blank=True
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_Scripts",
        null=True,
        blank=True
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="size_Scripts",
        null=True,
        blank=True
    )
    class Meta:
        pass

class No(TimeStampedModel):
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_No",
        null=True,
        blank=True
    )
    no = models.CharField(
        max_length=255
    )
    class Meta:
        pass

class NoScripts(TimeStampedModel):
    no = models.ForeignKey(
        No,
        on_delete=models.CASCADE,
        related_name="no_NoScripts"
    )
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_NoScripts"
    )
    class Meta:
        db_table = "noscripts"
        verbose_name = "NoScripts"
        verbose_name_plural = "NoScriptss"