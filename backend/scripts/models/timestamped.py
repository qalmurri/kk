from django.db import models
from scripts.utils import current_timestamp

class TimeStampedModel(models.Model):
    created_at = models.BigIntegerField(
        default=current_timestamp,
        editable=False
    )
    updated_at = models.BigIntegerField(
        null=True,
        blank=True
    )
    class Meta:
        abstract = True