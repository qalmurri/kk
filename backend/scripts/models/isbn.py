from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts

class Type(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )

class ISBN(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="type_ISBN"
    )
    isbn = models.CharField(
        max_length=122
    )