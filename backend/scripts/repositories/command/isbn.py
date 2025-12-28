from scripts.models import Isbn, TypeIsbn
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
    model = TypeIsbn

    @classmethod
    def create(cls, **data) -> TypeIsbn:
        return super().create(**data)

    @classmethod
    def update(cls, instance: TypeIsbn, **data) -> TypeIsbn:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance