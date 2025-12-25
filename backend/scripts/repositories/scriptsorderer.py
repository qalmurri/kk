from scripts.models import ScriptsOrderer
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsOrdererQueryRepository(BaseQueryRepository):
    model = ScriptsOrderer

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsOrdererCommandRepository(BaseCommandRepository):
    model = ScriptsOrderer

    @classmethod
    def create(cls, **data) -> ScriptsOrderer:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ScriptsOrderer, **data) -> ScriptsOrderer:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance