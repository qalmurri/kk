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