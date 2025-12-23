from scripts.models import Description
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class DescriptionQueryRepository(BaseQueryRepository):
    model = Description

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class DescriptionCommandRepository(BaseCommandRepository):
    model = Description

    @classmethod
    def create(cls, **data) -> Description:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Description, **data) -> Description:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance