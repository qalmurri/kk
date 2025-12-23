from rest_framework import serializers

COMPACT_FIELD_MAP = {
    #timestampt
    "created_at": "a",
    "updated_at": "r",
    "text": "z",
    "content": "x",
    "title": "o",
    "entry_date": "d",
    "finish_date": "e",
    "code": "b",
    "is_active": "f",
    "institute": "g",
    "isbn": "h",
    "label": "i",
    "no": "j",
    "name": "k",
    "orderer": "l",
    "size": "m",
    "type": "n",
    "user": "q",
    "part": "1",
    "thumbnail": "2",
    "length": "3",
    "height": "4",
    "width": "5",
    "x_axis": "6",
    "y_axis": "7",
    "notepart": "8",
    "descriptionpart": "9",
    "section": "10"
}

class BaseCompactSerializer(serializers.ModelSerializer):
    pass
#    def get_fields(self):
#        fields = super().get_fields()
#        compacted = {}
#
#        for field_name, field in fields.items():
#            if field_name == "id":
#                compacted[field_name] = field
#                continue
#
#            short_name = COMPACT_FIELD_MAP.get(field_name)
#            if short_name:
#                field.source = field_name
#                compacted[short_name] = field
#            else:
#                compacted[field_name] = field
#        return compacted
#   
#    def to_representation(self, instance):
#        data = super().to_representation(instance)
#        return {
#            k: v for k, v in data.items()
#            if v not in (None, [], {})
#        }

class PolicyBasedSerializer(BaseCompactSerializer):
    PROTECTED_FIELDS = set()

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop(
            "fields",
            None
        )
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(
                fields
            ) - self.PROTECTED_FIELDS
            existing = set(
                self.fields
            )

            invalid = allowed - existing
            if invalid:
                raise serializers.ValidationError(
                    f"Invalid fields requested: {invalid}"
                )

            for field in existing - allowed:
                self.fields.pop(
                    field
                )

class BaseReadSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )