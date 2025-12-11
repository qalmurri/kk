from django.db import models
from scripts.models.code import ScriptsStatusCode

class Purpose(models.Model): #MigrateDone
    label = models.IntegerField()
    code = models.ForeignKey(
        ScriptsStatusCode,
        on_delete=models.CASCADE,
    )
    sum = models.IntegerField()