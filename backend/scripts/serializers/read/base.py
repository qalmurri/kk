from scripts.serializers import PolicyBasedSerializer
from .mixins import DynamicFieldsMixin
#from .base_expandable import ExpandableFieldsMixin

class BaseReadSerializer(
    PolicyBasedSerializer,
    DynamicFieldsMixin,
    #ExpandableFieldsMixin
    ):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )