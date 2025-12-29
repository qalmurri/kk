from scripts.models.script import NoScripts
from scripts.repositories.base import BaseCommandRepository

class NoScriptsCommandRepository(BaseCommandRepository):
    model = NoScripts

    @classmethod
    def create(cls, **data) -> NoScripts:
        return super().create(**data)

    @classmethod
    def update(cls, instance: NoScripts, **data) -> NoScripts:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance