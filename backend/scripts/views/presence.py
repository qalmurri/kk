from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from scripts.repositories.command import SetUserOnlineStatusCommand

class PresenceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get("user")

        if not self.user or isinstance(self.user, AnonymousUser):
            await self.close()
            return

        await self.set_online(True)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "user") and not isinstance(self.user, AnonymousUser):
            await self.set_online(False)

    @database_sync_to_async
    def set_online(self, status: bool):
        return SetUserOnlineStatusCommand(
            user=self.user,
            is_online=status
        ).execute()