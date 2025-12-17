from django.db import models

class ScriptsStatusCode(models.Model):
    name = models.CharField(
        max_length=10,
    )
    label = models.IntegerField()