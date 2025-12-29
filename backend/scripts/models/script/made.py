from django.db import models
from django.contrib.auth import get_user_model
from scripts.models.base import TimeStampedModel
from .script import Script

User = get_user_model()

class SectionMade(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )
    class Meta:
        db_table = "sectionmade"
        verbose_name = "SectionMade"
        verbose_name_plural = "SectionMades"

class Made(TimeStampedModel): 
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsProcess"
    )
    sectionmade = models.ForeignKey(
        SectionMade,
        on_delete=models.CASCADE,
        related_name="section_ScriptsProcess"
    )
    class Meta:
        db_table = "made"
        verbose_name = "Made"
        verbose_name_plural = "Mades"

class ByMade(TimeStampedModel): 
    made = models.ForeignKey(
        Made,
        on_delete=models.CASCADE,
        related_name="scriptsprocess_By"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_By"
    )
    class Meta:
        db_table = "bymade"
        verbose_name = "ByMade"
        verbose_name_plural = "ByMades"
