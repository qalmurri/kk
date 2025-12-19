from django.db import models
from scripts.models.timestamped import TimeStampedModel

class ScriptsStatusCode(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )

class DescriptionPart(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )

class Institute(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )

class Label(TimeStampedModel):
    name = models.CharField(
        max_length=10,
    )

class NotePart(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )

class Part(TimeStampedModel):
    name = models.CharField(
        max_length=10,
    )

class Section(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )

class Size(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )

class Type(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )

class Orderer(TimeStampedModel):
    name = models.CharField(
        max_length=255
    )
    no = models.IntegerField(
        null=True,
        blank=True
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_Orderer",
        null=True,
        blank=True
    )