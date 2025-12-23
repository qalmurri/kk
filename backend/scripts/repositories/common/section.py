from scripts.models import Section
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class SectionQueryRepository(BaseQueryRepository):
    model = Section

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class SectionCommandRepository(BaseCommandRepository):
    model = Section

    @classmethod
    def create(cls, **data) -> Section:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Section, **data) -> Section:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance