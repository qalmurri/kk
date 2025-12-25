from scripts.models import Size, Institute
from .base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class SizeQueryRepository(BaseQueryRepository):
    model = Size

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class SizeCommandRepository(BaseCommandRepository):
    model = Size

    @classmethod
    def create(cls, **data) -> Size:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Size, **data) -> Size:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
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