from rest_framework import serializers

class PolicyBasedSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            for field in set(self.fields) - allowed:
                self.fields.pop(field)