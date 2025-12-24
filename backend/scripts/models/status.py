from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.script import Script

class Label(TimeStampedModel):
    name = models.CharField(
        max_length=10,
    )
    class Meta:
        pass

class ScriptsStatusCode(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )
    class Meta:
        pass

class Status(TimeStampedModel):
    scripts = models.ForeignKey(
        Script,
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
    class Meta:
        pass
