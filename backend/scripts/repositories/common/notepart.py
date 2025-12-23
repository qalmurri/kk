from scripts.models import NotePart
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class NotePartQueryRepository(BaseQueryRepository):
    model = NotePart

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class NotePartCommandRepository(BaseCommandRepository):
    model = NotePart

    @classmethod
    def create(cls, **data) -> NotePart:
        return super().create(**data)

    @classmethod
    def update(cls, instance: NotePart, **data) -> NotePart:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance