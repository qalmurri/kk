from scripts.models import Note, SectionNote, TextNote
from scripts.repositories.base import BaseQueryRepository

class NoteQueryRepository(BaseQueryRepository):
    model = Note

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class SectionNoteQueryRepository(BaseQueryRepository):
    model = SectionNote

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class TextNoteQueryRepository(BaseQueryRepository):
    model = TextNote

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )