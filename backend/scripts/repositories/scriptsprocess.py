from scripts.models import ScriptProcess, By, Section
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsProcessQueryRepository(BaseQueryRepository):
    model = ScriptProcess

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsProcessCommandRepository(BaseCommandRepository):
    model = ScriptProcess

    @classmethod
    def create(cls, **data) -> ScriptProcess:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ScriptProcess, **data) -> ScriptProcess:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

class ByQueryRepository(BaseQueryRepository):
    model = By

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ByCommandRepository(BaseCommandRepository):
    model = By

    @classmethod
    def create(cls, **data) -> By:
        return super().create(**data)

    @classmethod
    def update(cls, instance: By, **data) -> By:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

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