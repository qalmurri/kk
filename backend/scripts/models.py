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

class Order(TimeStampedModel):
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

class CoverColor(TimeStampedModel): #migrateDone
    color = models.CharField(
        max_length=255
    )

class CoverOther(TimeStampedModel):
    finishing = models.BooleanField(default=False)
    foil = models.BooleanField(default=False)
    emboss = models.BooleanField(default=False)

class CoverSpecifications(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_CoverSpecifications")
    covercolor = models.ForeignKey(
        CoverColor,
        on_delete=models.CASCADE,
        related_name="covercolor_CoverSpecifications",
        null=True,
        blank=True
        )
    coverother = models.ForeignKey(
        CoverOther,
        on_delete=models.CASCADE,
        related_name="coverother_CoverSpecifications",
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

class ScriptsOrderer(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsOrderer"
    )
    orderer = models.ForeignKey(
        Orderer,
        on_delete=models.CASCADE,
        related_name="orderer_ScriptsOrderer"
    )

class ScriptsInstitute(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsInstitute"
    )
    institute = models.ForeignKey(
        Institute,
        on_delete=models.CASCADE,
        related_name="institute_ScriptsInstitute"
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

class Size(TimeStampedModel): #MigrateDone
    size = models.CharField(
        max_length=255
    )

class ScriptsSize(TimeStampedModel):
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsSize"
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name="size_ScriptsSize"
    )

class ScriptsStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_ScriptsStatus"
    )
    purpose = models.ForeignKey(
        Purpose,
        on_delete=models.CASCADE,
        related_name="purpose_ScriptsStatus"
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