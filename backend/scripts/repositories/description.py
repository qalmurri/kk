from scripts.models import Description, SectionDescription, TextDescription
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

class DescriptionPartQueryRepository(BaseQueryRepository):
    model = SectionDescription

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class DescriptionPartCommandRepository(BaseCommandRepository):
    model = SectionDescription

    @classmethod
    def create(cls, **data) -> SectionDescription:
        return super().create(**data)

    @classmethod
    def update(cls, instance: SectionDescription, **data) -> SectionDescription:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
class TextQueryRepository(BaseQueryRepository):
    model = TextDescription

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class TextCommandRepository(BaseCommandRepository):
    model = TextDescription

    @classmethod
    def create(cls, **data) -> TextDescription:
        return super().create(**data)

    @classmethod
    def update(cls, instance: TextDescription, **data) -> TextDescription:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance