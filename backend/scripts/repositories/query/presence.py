from scripts.repositories.user_presence import (
    UserPresenceRepository
)

class GetUserPresenceQuery:
    def __init__(self, user):
        self.user = user

    def execute(self):
        return UserPresenceRepository.get_by_user(self.user)
