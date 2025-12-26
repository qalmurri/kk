from scripts.models import Note, SectionNote, TextNote
from scripts.repositories.base import BaseQueryRepository

class NoteQueryRepository(BaseQueryRepository):
    model = Note

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class NotePartQueryRepository(BaseQueryRepository):
    model = SectionNote

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ContentQueryRepository(BaseQueryRepository):
    model = TextNote

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )