from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.script import Script

class Type(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )
    class Meta:
        db_table = "type"
        verbose_name = "Type"
        verbose_name_plural = "Types"
        ordering = ["name"]

class Isbn(TimeStampedModel):
    scripts = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="type_ISBN"
    )
    isbn = models.CharField(
        max_length=20
    )
    class Meta:
        db_table = "isbn"
        verbose_name = "Isbn"
        verbose_name_plural = "Isbns"
        ordering = ["scripts", "type"]
        indexes = [
            models.Index(fields=["scripts"]),
            models.Index(fields=["type"]),
        ]