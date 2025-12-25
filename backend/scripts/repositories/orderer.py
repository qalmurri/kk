from scripts.models import Orderer, ScriptsOrderer
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class OrdererQueryRepository(BaseQueryRepository):
    model = Orderer

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class OrdererCommandRepository(BaseCommandRepository):
    model = Orderer

    @classmethod
    def create(cls, **data) -> Orderer:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Orderer, **data) -> Orderer:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
class ScriptsOrdererQueryRepository(BaseQueryRepository):
    model = ScriptsOrderer

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsOrdererCommandRepository(BaseCommandRepository):
    model = ScriptsOrderer

    @classmethod
    def create(cls, **data) -> ScriptsOrderer:
        return super().create(**data)

    @classmethod
    def update(cls, instance: ScriptsOrderer, **data) -> ScriptsOrderer:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance