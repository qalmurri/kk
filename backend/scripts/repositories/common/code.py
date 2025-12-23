from scripts.models import ScriptsStatusCode
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsStatusCodeQueryRepository(BaseQueryRepository):
    model = ScriptsStatusCode

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsStatusCodeCommandRepository(BaseCommandRepository):
    model = ScriptsStatusCode

    @classmethod
    def create(cls, **data) -> ScriptsStatusCode:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ScriptsStatusCode, **data) -> ScriptsStatusCode:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance