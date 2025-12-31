from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.forms.models import model_to_dict

from scripts.models import ActivityLog, TimeStampedModel

from scripts.serializers.read import ActivityReadSerializer
from scripts.services.notification import NotificationService

from django.contrib.auth import get_user_model
User = get_user_model()
userid = User.objects.filter(id=1).first()

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
        print("create data model")
        activity = ActivityLog.objects.create(
            user=userid,
            model_name=model_name,
            object_id=str(instance.pk),
            action=1, #create
            changes=model_to_dict(instance)
        )
        if activity.user and hasattr(activity.user, "id"):
            payload = ActivityReadSerializer(activity).data
            print("kirim websocket")
            NotificationService.notify_user(
                user_id=activity.user.id,
                payload=payload
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
            activity = ActivityLog.objects.create(
                user=None,
                model_name=model_name,
                object_id=str(instance.pk),
                action=2,# update
                changes=diff
            )
            if activity.user and hasattr(activity.user, "id"):
                payload = ActivityReadSerializer(activity).data
                NotificationService.notify_user(
                    user_id=activity.user.id,
                    payload=payload
                )


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if not issubclass(sender, TimeStampedModel):
        return

    activity = ActivityLog.objects.create(
        user=None,
        model_name=sender.__name__,
        object_id=str(instance.pk),
        action=3, #delete
        changes=model_to_dict(instance)
    )

    if activity.user and hasattr(activity.user, "id"):
        payload = ActivityReadSerializer(activity).data
        NotificationService.notify_user(
            user_id=activity.user.id,
            payload=payload
        )
