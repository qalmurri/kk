from django.db import models
from scripts.models.base import TimeStampedModel
from .script import Script
from .common import Institute

class Orderer(TimeStampedModel):
    '''pivot: relasi orderer & script'''
    name = models.CharField(
        max_length=255
    )
    no = models.IntegerField(
        null=True,
        blank=True
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_Orderer",
        null=True,
        blank=True
    )
    class Meta:
        db_table = "orderer"
        verbose_name = "Orderer"
        verbose_name_plural = "Orderers"

class ScriptsOrderer(TimeStampedModel): 
    '''pivot: relasi orderer & script'''
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsOrderer"
    )
    orderer = models.ForeignKey(
        Orderer,
        on_delete=models.CASCADE,
        related_name="orderer_ScriptsOrderer"
    )
    class Meta:
        db_table = "scriptsorderer"
        verbose_name = "ScriptsOrderer"
        verbose_name_plural = "ScriptsOrderers"