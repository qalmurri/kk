from rest_framework import serializers

class UserPresenceWriteSerializer(serializers.Serializer):
    is_online = serializers.BooleanField()
