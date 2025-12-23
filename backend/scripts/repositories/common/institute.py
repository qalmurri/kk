from scripts.models import Institute
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class InstituteQueryRepository(BaseQueryRepository):
    model = Institute

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class InstituteCommandRepository(BaseCommandRepository):
    model = Institute

    @classmethod
    def create(cls, **data) -> Institute:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Institute, **data) -> Institute:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance