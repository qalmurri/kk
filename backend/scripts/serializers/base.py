from rest_framework import serializers

COMPACT_FIELD_MAP = {
    #timestampt
    "created_at": "ca",
    "updated_at": "ua",
    "title": "t",
    "alias": "a",
    "is_active": "ia",
    "entry_date": "ed",
    "finish_date": "fd",
    "institute": "i",
    "size": "s",
    "orderer": "o",
    "name": "n",
    "labelstatus": "ls",
    "sectionstatus": "ss",
    "sectionflag": "sf",
    "sectiondescription": "sd",
    "sectionmade": "sm",
    "sectionnote": "sn",
    "typeisbn": "ti",
    "isbn": "i_",
    "user": "u",
    "textdescription": "td",
    "text": "te",
    "thumbnail": "th",
    "length": "l",
    "height": "h",
    "width": "w",
    "x_axis": "x",
    "y_axis": "y",

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
