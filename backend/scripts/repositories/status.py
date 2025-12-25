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
    
from scripts.models import ScriptsStatusCode
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsStatusCodeQueryRepository(BaseQueryRepository):
    model = ScriptsStatusCode

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsStatusCodeCommandRepository(BaseCommandRepository):
    model = ScriptsStatusCode

    @classmethod
    def create(cls, **data) -> ScriptsStatusCode:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ScriptsStatusCode, **data) -> ScriptsStatusCode:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
from scripts.models import Label
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class LabelQueryRepository(BaseQueryRepository):
    model = Label

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class LabelCommandRepository(BaseCommandRepository):
    model = Label

    @classmethod
    def create(cls, **data) -> Label:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Label, **data) -> Label:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance