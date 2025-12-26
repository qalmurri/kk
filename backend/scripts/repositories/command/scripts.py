from django.db.models import Q
from scripts.models import Script
from scripts.repositories.base import BaseCommandRepository
    
class ScriptsCommandRepository(BaseCommandRepository):
    model = Script

    @classmethod
    def create(cls, **data) -> Script:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Script, **data) -> Script:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance