from scripts.models import Flag
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class FlagQueryRepository(BaseQueryRepository):
    model = Flag

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class FlagCommandRepository(BaseCommandRepository):
    model = Flag

    @classmethod
    def create(cls, **data) -> Flag:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Flag, **data) -> Flag:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance