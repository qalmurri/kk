from django.shortcuts import get_object_or_404
from scripts.models import Purpose

class PurposeQueryRepository:
    @staticmethod
    def list_all():
        return Purpose.objects.all()
    
    @staticmethod
    def get_by_id(id: int) -> Purpose:
        return get_object_or_404(
            Purpose,
            id=id
        )
    
    @staticmethod
    def get_by_code(code: int):
        return Purpose.objects.filter(
            code=code
        )

class PurposeCommandRepository:
    @staticmethod
    def create(code: int, purpose: str) -> Purpose:
        return Purpose.objects.create(
            code=code,
            purpose=purpose
        )

    @staticmethod
    def update_fast(id: int, **kwargs) -> int:
        return Purpose.objects.filter(
            id=id
        ).update(
            **kwargs
        )

    @staticmethod
    def update_safe(id: int, **kwargs) -> Purpose:
        obj = get_object_or_404(
            Purpose,
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