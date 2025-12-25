from scripts.models import Status
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class StatusQueryRepository(BaseQueryRepository):
    model = Status

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class StatusCommandRepository(BaseCommandRepository):
    model = Status

    @classmethod
    def create(cls, **data) -> Status:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Status, **data) -> Status:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance