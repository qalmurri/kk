from scripts.models import CoverColor
from django.shortcuts import get_object_or_404
    
class CoverColorQueryRepository:
    @staticmethod
    def list_all():
        return CoverColor.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return CoverColor.objects.get(
            id=id
        )
   
class CoverColorCommandRepository:
    @staticmethod
    def create(color: str) -> CoverColor:
        return CoverColor.objects.create(
            color=color
        )

    @staticmethod
    def update_fast(id: int, **kwargs) -> int:
        return CoverColor.objects.filter(
            id=id
        ).update(
            **kwargs
        )

    @staticmethod
    def update_safe(id: int, **kwargs) -> CoverColor:
        obj = get_object_or_404(
            CoverColor,
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