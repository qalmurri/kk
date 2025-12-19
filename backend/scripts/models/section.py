from django.db import models

class Section(models.Model):
    name = models.CharField(
        max_length=10
    )