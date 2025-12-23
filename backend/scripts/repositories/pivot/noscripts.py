from scripts.models import NoScripts
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class NoScriptsQueryRepository(BaseQueryRepository):
    model = NoScripts

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

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