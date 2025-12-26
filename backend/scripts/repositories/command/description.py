from scripts.models import Description, SectionDescription, TextDescription
from scripts.repositories.base import BaseCommandRepository

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