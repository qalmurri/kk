from scripts.models import Note, SectionNote, TextNote
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

class NotePartQueryRepository(BaseQueryRepository):
    model = SectionNote

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class NotePartCommandRepository(BaseCommandRepository):
    model = SectionNote

    @classmethod
    def create(cls, **data) -> SectionNote:
        return super().create(**data)

    @classmethod
    def update(cls, instance: SectionNote, **data) -> SectionNote:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

class ContentQueryRepository(BaseQueryRepository):
    model = TextNote

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ContentCommandRepository(BaseCommandRepository):
    model = TextNote

    @classmethod
    def create(cls, **data) -> TextNote:
        return super().create(**data)

    @classmethod
    def update(cls, instance: TextNote, **data) -> TextNote:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance