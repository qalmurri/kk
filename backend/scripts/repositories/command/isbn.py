from scripts.models import Isbn, Type
from scripts.repositories.base import BaseCommandRepository

class IsbnCommandRepository(BaseCommandRepository):
    model = Isbn

    @classmethod
    def create(cls, **data) -> Isbn:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Isbn, **data) -> Isbn:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance

class TypeIsbnCommandRepository(BaseCommandRepository):
    model = Type

    @classmethod
    def create(cls, **data) -> Type:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Type, **data) -> Type:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance