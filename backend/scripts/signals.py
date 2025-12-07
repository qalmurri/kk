from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.forms.models import model_to_dict

from .models import *
from .models import ActivityLog

_PREVIOUS_STATE = {}

@receiver(pre_save)
def cache_previous_state(sender, instance, **kwargs):
    if not issubclass(sender, TimeStampedModel):
        return

    if instance.pk:
        try:
            old = sender.objects.get(pk=instance.pk)
            _PREVIOUS_STATE[instance.pk] = model_to_dict(old)
        except sender.DoesNotExist:
            pass


@receiver(post_save)
def log_create_update(sender, instance, created, **kwargs):
    if not issubclass(sender, TimeStampedModel):
        return

    model_name = sender.__name__

    if created:
        ActivityLog.objects.create(
            user=None,
            model_name=model_name,
            object_id=str(instance.pk),
            action=1, #create
            changes=model_to_dict(instance)
        )
    else:
        old = _PREVIOUS_STATE.get(instance.pk, {})
        new = model_to_dict(instance)

        diff = {
            field: {"old": old.get(field), "new": new.get(field)}
            for field in new
            if old.get(field) != new.get(field)
        }

        if diff:
            ActivityLog.objects.create(
                user=None,
                model_name=model_name,
                object_id=str(instance.pk),
                action=2,# update
                changes=diff
            )


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if not issubclass(sender, TimeStampedModel):
        return

    ActivityLog.objects.create(
        user=None,
        model_name=sender.__name__,
        object_id=str(instance.pk),
        action=3, #delete
        changes=model_to_dict(instance)
    )
