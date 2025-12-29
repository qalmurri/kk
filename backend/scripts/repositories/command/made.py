from scripts.models.script import Made, ByMade, SectionMade
from scripts.repositories.base import BaseCommandRepository

class MadeCommandRepository(BaseCommandRepository):
    model = Made

    @classmethod
    def create(cls, **data) -> Made:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Made, **data) -> Made:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

class ByMadeCommandRepository(BaseCommandRepository):
    model = ByMade

    @classmethod
    def create(cls, **data) -> ByMade:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ByMade, **data) -> ByMade:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

class SectionMadeCommandRepository(BaseCommandRepository):
    model = SectionMade

    @classmethod
    def create(cls, **data) -> SectionMade:
        return super().create(**data)

    @classmethod
    def update(cls, instance: SectionMade, **data) -> SectionMade:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance