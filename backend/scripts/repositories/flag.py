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