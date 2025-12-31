from rest_framework import serializers
from scripts.models import UserPresence

class UserPresenceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPresence
        fields = (
            "user",
            "is_online",
            "last_seen",
        )
