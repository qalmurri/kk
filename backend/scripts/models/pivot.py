from django.db import models
from django.contrib.auth import get_user_model
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import (
    Scripts,
    No
)
from scripts.models.common import (
    Orderer,
    Section,
    DescriptionPart,
    ScriptsStatusCode,
    Label,
    NotePart
)

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

class Description(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Description"
    )
    descriptionpart = models.ForeignKey(
        DescriptionPart,
        on_delete=models.CASCADE,
        related_name="descriptionpart_Description"
    )

class Status(TimeStampedModel): #MigrateDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Status"
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        related_name="label_Status"
    )
    code = models.ForeignKey(
        ScriptsStatusCode,
        on_delete=models.CASCADE,
        related_name="code_Status"
    )

class Note(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Note"
    )
    notepart = models.ForeignKey(
        NotePart,
        on_delete=models.CASCADE,
        related_name="notepart_Note"
    )

