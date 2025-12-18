from django.db import models

class Label(models.Model):
    name = models.CharField(
        max_length=10,
    )