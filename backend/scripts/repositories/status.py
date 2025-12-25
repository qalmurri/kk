from scripts.models import Status, LabelStatus, SectionStatus
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

class ScriptsStatusCodeQueryRepository(BaseQueryRepository):
    model = SectionStatus

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsStatusCodeCommandRepository(BaseCommandRepository):
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

class LabelQueryRepository(BaseQueryRepository):
    model = LabelStatus

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class LabelCommandRepository(BaseCommandRepository):
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