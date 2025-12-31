from scripts.models import UserPresence

class UserPresenceRepository:

    @staticmethod
    def get_or_create_by_user(user):
        return UserPresence.objects.get_or_create(user=user)

    @staticmethod
    def save(presence):
        presence.save()
        return presence

    @staticmethod
    def get_by_user(user):
        return UserPresence.objects.filter(user=user).first()
