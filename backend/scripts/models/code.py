from django.db import models

class ScriptsStatusCode(models.Model):
    code = models.CharField(
        max_length=10,
    )