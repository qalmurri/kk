from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.pivot import (
    Note,
    Description
)
from scripts.models.common import (
    Part,
    Type
)

class CoverBook(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Cover"
    )
    thumbnail = models.CharField(max_length=255)
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    x_axis = models.IntegerField(default=0)
    y_axis = models.IntegerField(default=0)

class Text(TimeStampedModel):
    description = models.ForeignKey(
        Description,
        on_delete=models.CASCADE,
        related_name="description_Text"
    )
    text = models.CharField(
        max_length=255
    )

class Flag(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_Flag"
    )
    is_active = models.BooleanField(
        default=False
    )
    part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
        related_name="part_Flag"
    )

class ISBN(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ISBN"
    )
    isbn = models.CharField(
        max_length=122
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name="type_ISBN"
    )

class Content(TimeStampedModel):
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="note_Content"
    )
    content = models.CharField(
        max_length=255
    )

