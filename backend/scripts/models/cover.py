from django.db import models
from scripts.models.timestamped import TimeStampedModel
from scripts.models.scripts import Scripts
from scripts.models.status import Status
from django.contrib.auth import get_user_model

User = get_user_model()

class CoverStatus(TimeStampedModel): #PurposeDone
    scripts = models.ForeignKey(
        Scripts,
        on_delete=models.CASCADE,
        related_name="scripts_CoverStatus"
    )
    purpose = models.ForeignKey(
        Status,
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