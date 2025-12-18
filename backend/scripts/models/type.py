from django.db import models

class Type(models.Model):
    name = models.CharField(
        max_length=10
    )