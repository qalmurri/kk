from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts, No
from scripts.models.orderer import Orderer
from scripts.models.purpose import Purpose
from scripts.models.code import ScriptsStatusCode

class NoScripts(TimeStampedModel):
    no = models.ForeignKey(
        No,
        on_delete=models.CASCADE,
        related_name="no_NoScripts"
    )
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_NoScripts"
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

class ScriptsStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsStatus"
    )
    scriptsstatuscode = models.ForeignKey(
        ScriptsStatusCode,
        on_delete=models.CASCADE,
        related_name="scriptsstatuscode_ScriptsStatus"
    )
    
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ScriptsStatus"
    )


