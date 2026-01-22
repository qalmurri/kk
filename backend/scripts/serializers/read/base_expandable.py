import importlib
from rest_framework import serializers
from scripts.includes.script import SCRIPT_INCLUDES

class ExpandableFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        includes = self.context.get("includes", set())

        for key, config in SCRIPT_INCLUDES.items():
            if key not in includes:
                self.fields.pop(key, None)
                continue

            module, cls_name = config["serializer"].rsplit(".", 1)
            serializer_cls = getattr(
                importlib.import_module(module),
                cls_name
            )

            self.fields[key] = serializer_cls(
                source=config["source"],
                many=config.get("many", False),
                read_only=True,
                context=self.context,  # 🔥 penting
            )

    def get_fields(self):
        fields = super().get_fields()

        includes = self.context.get("includes", set())

        for key in includes:
            config = SCRIPT_INCLUDES.get(key)
            if not config:
                continue

            module, cls_name = config["serializer"].rsplit(".", 1)
            serializer_cls = getattr(
                importlib.import_module(module),
                cls_name
            )

            fields[key] = serializer_cls(
                source=config["source"],
                many=config.get("many", False),
                read_only=True,
                context=self.context,
            )

        return fields