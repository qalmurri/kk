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