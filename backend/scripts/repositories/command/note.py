from scripts.models.script import Note, SectionNote, TextNote
from scripts.repositories.base import BaseCommandRepository

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

class SectionNoteCommandRepository(BaseCommandRepository):
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

class TextNoteCommandRepository(BaseCommandRepository):
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