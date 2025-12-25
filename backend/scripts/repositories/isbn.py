from scripts.models import ISBN
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ISBNQueryRepository(BaseQueryRepository):
    model = ISBN

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ISBNCommandRepository(BaseCommandRepository):
    model = ISBN

    @classmethod
    def create(cls, **data) -> ISBN:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ISBN, **data) -> ISBN:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
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