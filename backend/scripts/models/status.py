from django.db import models
from scripts.models.code import ScriptsStatusCode
from scripts.models.scripts import Scripts
from scripts.models.timestamped import TimeStampedModel

class Status(TimeStampedModel): #MigrateDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Status"
    )
    label = models.IntegerField()
    code = models.ForeignKey(
        ScriptsStatusCode,
        on_delete=models.CASCADE,
        related_name="code_Status"
    )