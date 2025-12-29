from scripts.serializers import PolicyBasedSerializer

class BaseReadSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )