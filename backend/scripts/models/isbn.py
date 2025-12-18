from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.type import Type

class ISBN(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    isbn = models.CharField(
        max_length=122
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="type_ISBN"
    )
