from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.orderer import Orderer
from scripts.models.no import No
from scripts.models.label import Label
from scripts.models.section import Section
from django.contrib.auth import get_user_model

User = get_user_model()

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

class ScriptsProcess(TimeStampedModel): 
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsProcess"
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="section_ScriptsProcess"
    )

class By(TimeStampedModel): 
    scriptsprocess = models.ForeignKey(
        ScriptsProcess,
        on_delete=models.CASCADE,
        related_name="scriptsprocess_By"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_By"
    )