from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.purpose import Purpose
from scripts.models.institute import Institute
from scripts.models.size import Size

class Order(TimeStampedModel): #nomer dibuat
    title = models.CharField(
        max_length=255
    )
    status = models.BooleanField(default=False)

class Scripts(TimeStampedModel): #MigrateDone
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_Scripts",
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=255
    )
    entry_date = models.DateField(
        null=True,
        blank=True
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_Scripts",
        null=True,
        blank=True
    )

    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="size_Scripts",
        null=True,
        blank=True
    )

class ScriptsDescription(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsDescription"
    )
    description = models.CharField(
        max_length=255
    )

class Completeness(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Completeness"
    )
    file = models.BooleanField(default=False)
    editor = models.BooleanField(default=False)
    photo = models.BooleanField(default=False)
    preface = models.BooleanField(default=False) #kata pengantar
    cv = models.BooleanField(default=False)
    loc = models.BooleanField(default=False) #list of contents / daftar isi
    synopsis = models.BooleanField(default=False)
    references = models.BooleanField(default=False) #daftar pustaka

class ScriptsIsbn(TimeStampedModel): #PurposeDone #MigrateDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsIsbn"
    )
    isbn = models.CharField(
        max_length=20
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ScriptsIsbn"
    )