from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.orderer import Orderer
from scripts.models.size import Size
from scripts.models.purpose import Purpose

class ScriptsOrderer(TimeStampedModel): 
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsOrderer"
    )
    orderer = models.ForeignKey(
        Orderer,
        on_delete=models.CASCADE,
        related_name="orderer_ScriptsOrderer"
    )

class ScriptsSize(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsSize"
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="size_ScriptsSize"
    )

class ScriptsStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsStatus"
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ScriptsStatus"
    )

class ProductionEbookStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ProductionEbookStatus"
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ProductionEbookStatus"
    )

