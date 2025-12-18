from django.db import models
from scripts.models.code import ScriptsStatusCode
from scripts.models.scripts import Scripts
from scripts.models.timestamped import TimeStampedModel
from scripts.models.label import Label

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