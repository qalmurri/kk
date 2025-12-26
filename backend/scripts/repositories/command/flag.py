from scripts.models import Flag, Part
from scripts.repositories.base import BaseCommandRepository

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