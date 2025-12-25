from scripts.models import Description
from .base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class DescriptionQueryRepository(BaseQueryRepository):
    model = Description

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class DescriptionCommandRepository(BaseCommandRepository):
    model = Description

    @classmethod
    def create(cls, **data) -> Description:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Description, **data) -> Description:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
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
    
from scripts.models import Text
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class TextQueryRepository(BaseQueryRepository):
    model = Text

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class TextCommandRepository(BaseCommandRepository):
    model = Text

    @classmethod
    def create(cls, **data) -> Text:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Text, **data) -> Text:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance