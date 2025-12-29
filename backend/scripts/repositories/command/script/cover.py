from scripts.models.script import Cover
from scripts.repositories.command import BaseCommandRepository

class CoverBookCommandRepository(BaseCommandRepository):
    model = Cover

    @classmethod
    def create(cls, **data) -> Cover:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Cover, **data) -> Cover:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance