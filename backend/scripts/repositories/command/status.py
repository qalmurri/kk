from scripts.models.script import Status, LabelStatus, SectionStatus
from scripts.repositories.base import BaseCommandRepository

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

class SectionStatusCommandRepository(BaseCommandRepository):
    model = SectionStatus

    @classmethod
    def create(cls, **data) -> SectionStatus:
        return super().create(**data)

    @classmethod
    def update(cls, instance: SectionStatus, **data) -> SectionStatus:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

class LabelStatusCommandRepository(BaseCommandRepository):
    model = LabelStatus

    @classmethod
    def create(cls, **data) -> LabelStatus:
        return super().create(**data)

    @classmethod
    def update(cls, instance: LabelStatus, **data) -> LabelStatus:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance