from django.db import models
from django.contrib.auth import get_user_model
from scripts.utils import current_timestamp

User = get_user_model()

class ActivityLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    model_name = models.CharField(
        max_length=255
    )
    object_id = models.CharField(
        max_length=255
    )
    action = models.IntegerField()
    changes = models.JSONField(
        null=True,
        blank=True
    )
    created_at = models.BigIntegerField(
        default=current_timestamp,
        editable=False
    )