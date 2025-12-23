from scripts.models import Note
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class NoteQueryRepository(BaseQueryRepository):
    model = Note

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class NoteCommandRepository(BaseCommandRepository):
    model = Note

    @classmethod
    def create(cls, **data) -> Note:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Note, **data) -> Note:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance