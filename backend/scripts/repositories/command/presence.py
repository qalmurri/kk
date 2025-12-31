from django.utils import timezone
from scripts.repositories.user_presence import (
    UserPresenceRepository
)

class SetUserOnlineStatusCommand:
    def __init__(self, user, is_online: bool):
        self.user = user
        self.is_online = is_online

    def execute(self):
        presence, _ = UserPresenceRepository.get_or_create_by_user(
            self.user
        )
        presence.is_online = self.is_online
        presence.last_seen = timezone.now()
        return UserPresenceRepository.save(presence)
