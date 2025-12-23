from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.common import Institute

class Orderer(TimeStampedModel):
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