from scripts.models import ScriptsProcess
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsProcessQueryRepository(BaseQueryRepository):
    model = ScriptsProcess

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsProcessCommandRepository(BaseCommandRepository):
    model = ScriptsProcess

    @classmethod
    def create(cls, **data) -> ScriptsProcess:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ScriptsProcess, **data) -> ScriptsProcess:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance