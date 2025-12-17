from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models import Scripts, ScriptsStatusCode

class ISBN(TimeStampedModel): #MigrateDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    isbn = models.CharField(
        max_length=122
    )
    code = models.ForeignKey(
        ScriptsStatusCode,
        on_delete=models.CASCADE,
        related_name="code_ISBN"
    )