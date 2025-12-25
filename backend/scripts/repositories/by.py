from scripts.models import By
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ByQueryRepository(BaseQueryRepository):
    model = By

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ByCommandRepository(BaseCommandRepository):
    model = By

    @classmethod
    def create(cls, **data) -> By:
        return super().create(**data)

    @classmethod
    def update(cls, instance: By, **data) -> By:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance