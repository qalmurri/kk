from scripts.serializers import PolicyBasedSerializer

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "updated_at",
        )