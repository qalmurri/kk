class DynamicFieldsMixin:
    print("DynamicFieldsMixin")
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields)
            for field in existing - allowed:
                self.fields.pop(field)
