from scripts.models import CoverBook
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class CoverBookQueryRepository(BaseQueryRepository):
    model = CoverBook

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class CoverBookCommandRepository(BaseCommandRepository):
    model = CoverBook

    @classmethod
    def create(cls, **data) -> CoverBook:
        return super().create(**data)

    @classmethod
    def update(cls, instance: CoverBook, **data) -> CoverBook:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance