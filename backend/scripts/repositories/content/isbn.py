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