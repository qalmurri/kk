from django.db import models
from django.contrib.auth import get_user_model
from scripts.models.timestamped import TimeStampedModel
from scripts.models.script import Script

User = get_user_model()

class Section(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )
    class Meta:
        pass

class ScriptsProcess(TimeStampedModel): 
    scripts = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsProcess"
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="section_ScriptsProcess"
    )
    class Meta:
        pass

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
    class Meta:
        pass
