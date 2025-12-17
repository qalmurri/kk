from django.shortcuts import get_object_or_404
from scripts.models import Status

class StatusQueryRepository:
    @staticmethod
    def list_all():
        return Status.objects.all()
    
    @staticmethod
    def get_by_id(id: int) -> Status:
        return get_object_or_404(
            Status,
            id=id
        )
    
    @staticmethod
    def get_by_code(code: int):
        return Status.objects.filter(
            code=code
        )

class StatusCommandRepository:
    @staticmethod
    def create(code: int, purpose: str) -> Status:
        return Status.objects.create(
            code=code,
            purpose=purpose
        )

    @staticmethod
    def update_fast(id: int, **kwargs) -> int:
        return Status.objects.filter(
            id=id
        ).update(
            **kwargs
        )

    @staticmethod
    def update_safe(id: int, **kwargs) -> Status:
        obj = get_object_or_404(
            Status,
            id=id
        )
        for key, value in kwargs.items():
            setattr(
                obj,
                key,
                value
            )
        obj.save()
        return obj