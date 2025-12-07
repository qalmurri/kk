from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import current_timestamp
import uuid

class User(AbstractUser):
    """
    python manage.py shell
    from scripts.models import User
    User.objects.create_user(username="andi", password="12345")
    """
    first_name = None
    last_name = None
    last_login = None
    public_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

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

class Purpose(TimeStampedModel): #MigrateDone
    code = models.IntegerField(db_index=True)
    purpose = models.CharField(
        max_length=255
    )
    class Meta:
        unique_together = (
            'code',
            'purpose'
        )

class Institute(TimeStampedModel): #MigrateDone
    institute = models.CharField(
        max_length=255
    )

class Orderer(TimeStampedModel): #MigrateDone
    orderer = models.CharField(
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

class Scripts(TimeStampedModel): #MigrateDone
    title = models.CharField(
        max_length=255
    )
    entry_date = models.DateField(
        null=True,
        blank=True
    )
    completion_date = models.DateField(
        null=True,
        blank=True
    )

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

class ScriptOrderer(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptOrderer"
    )
    orderer = models.ForeignKey(
        Orderer,
        on_delete=models.CASCADE,
        related_name="orderer_ScriptOrderer"
    )

class ScriptInstitute(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptInstitute"
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_ScriptInstitute"
    )

class ScriptsDescription(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptDescription"
    )
    description = models.CharField(
        max_length=255
    )

class Size(TimeStampedModel): #MigrateDone
    size = models.CharField(
        max_length=255
    )

class ScriptSize(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptSize"
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="size_ScriptSize"
    )

class ScriptStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptStatus"
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ScriptStatus"
    )

class CoverStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_CoverStatus"
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_CoverStatus"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

class CoverStatusDescription(TimeStampedModel):
    coverstatus = models.ForeignKey(
        CoverStatus,
        on_delete=models.CASCADE,
        related_name="coverstatus_CoverStatusDescription"
    )
    description = models.CharField(
        max_length=255
    )

class ProductionEbookStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ProductionEbookStatus"
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ProductionEbookStatus"
    )

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