from scripts.models import Part
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class PartQueryRepository(BaseQueryRepository):
    model = Part

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class PartCommandRepository(BaseCommandRepository):
    model = Part

    @classmethod
    def create(cls, **data) -> Part:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Part, **data) -> Part:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance