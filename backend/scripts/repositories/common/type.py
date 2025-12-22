from django.db.models import Q
from scripts.models import Type
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class TypeQueryRepository(BaseQueryRepository):
    model = Type

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class TypeCommandRepository(BaseCommandRepository):
    model = Type

    @classmethod
    def create(cls, **data) -> Type:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Type, **data) -> Type:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance