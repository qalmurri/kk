from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models import Scripts

class ISBN(TimeStampedModel): #MigrateDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    isbn = models.CharField(
        max_length=122
    )
    type = models.IntegerField()