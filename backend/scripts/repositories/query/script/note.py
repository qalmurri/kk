from scripts.models.script import Note, SectionNote, TextNote
from scripts.repositories.query import BaseQueryRepository

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