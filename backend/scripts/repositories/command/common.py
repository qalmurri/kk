from scripts.models.script import Size, Institute
from scripts.repositories.base import BaseCommandRepository

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