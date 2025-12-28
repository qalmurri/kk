from django.db import models
from scripts.models.base import TimeStampedModel
from scripts.models.script import Script

class TypeIsbn(TimeStampedModel):
    name = models.CharField(
        max_length=10
    )
    class Meta:
        db_table = "typeisbn"
        verbose_name = "TypeIsbn"
        verbose_name_plural = "TypeIsbns"
        ordering = ["name"]

class Isbn(TimeStampedModel):
    script = models.ForeignKey(
        Script,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    typeisbn = models.ForeignKey(
        TypeIsbn,
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