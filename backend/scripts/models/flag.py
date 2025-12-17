from django.db import models
from scripts.models.scripts import Scripts
from scripts.models.timestamped import TimeStampedModel

class Flag(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Bool"
    )
    is_active = models.BooleanField(default=False)
    label = models.IntegerField()