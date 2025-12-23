from scripts.models import Label
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class LabelQueryRepository(BaseQueryRepository):
    model = Label

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class LabelCommandRepository(BaseCommandRepository):
    model = Label

    @classmethod
    def create(cls, **data) -> Label:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Label, **data) -> Label:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance