from scripts.models import DescriptionPart
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class DescriptionPartQueryRepository(BaseQueryRepository):
    model = DescriptionPart

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class DescriptionPartCommandRepository(BaseCommandRepository):
    model = DescriptionPart

    @classmethod
    def create(cls, **data) -> DescriptionPart:
        return super().create(**data)

    @classmethod
    def update(cls, instance: DescriptionPart, **data) -> DescriptionPart:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance