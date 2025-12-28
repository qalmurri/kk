from scripts.models import Flag, SectionFlag
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

class SectionFlagCommandRepository(BaseCommandRepository):
    model = SectionFlag

    @classmethod
    def create(cls, **data) -> SectionFlag:
        return super().create(**data)

    @classmethod
    def update(cls, instance: SectionFlag, **data) -> SectionFlag:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance