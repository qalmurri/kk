from django.db import models

class Part(models.Model):
    name = models.CharField(
        max_length=10,
    )