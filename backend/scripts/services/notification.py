from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class NotificationService:
    @staticmethod
    def notify_user(user_id: int, payload: dict):
        print("mulai notifikasi chanler")
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            f"notifications_user_{user_id}",
            {
                "type": "notify",
                "payload": payload
            }
        )
