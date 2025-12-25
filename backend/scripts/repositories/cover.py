from scripts.models import Cover
from .base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class CoverBookQueryRepository(BaseQueryRepository):
    model = Cover

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class CoverBookCommandRepository(BaseCommandRepository):
    model = Cover

    @classmethod
    def create(cls, **data) -> Cover:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Cover, **data) -> Cover:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance