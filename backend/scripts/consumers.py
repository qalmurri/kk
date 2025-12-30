from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser
from scripts.models import UserPresence

class PresenceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get("user")
    
        if not self.user or isinstance(self.user, AnonymousUser):
            await self.close()
            return
    
        await self.set_online(True)
        print("WS USER:", self.user)
        await self.accept()

    async def disconnect(self, close_code):
        user = getattr(self, "user", None)
        if user and not isinstance(user, AnonymousUser):
            await self.set_online(False)

    @database_sync_to_async
    def set_online(self, status):
        presence, _ = UserPresence.objects.get_or_create(user=self.user)
        presence.is_online = status
        presence.last_seen = timezone.now()
        presence.save()