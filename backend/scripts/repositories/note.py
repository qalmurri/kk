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
    
from scripts.models import Content
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ContentQueryRepository(BaseQueryRepository):
    model = Content

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ContentCommandRepository(BaseCommandRepository):
    model = Content

    @classmethod
    def create(cls, **data) -> Content:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Content, **data) -> Content:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance