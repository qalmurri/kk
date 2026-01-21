from scripts.serializers import PolicyBasedSerializer
from .mixins import DynamicFieldsMixin

class BaseReadSerializer(PolicyBasedSerializer, DynamicFieldsMixin):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )