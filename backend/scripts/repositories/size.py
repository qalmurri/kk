from django.shortcuts import get_object_or_404
from scripts.models import Size

class SizeQueryRepository:
    @staticmethod
    def list_all():
        return Size.objects.all()
    
    @staticmethod
    def get_by_id(id: int) -> Size:
        return get_object_or_404(
            Size,
            id=id
        )
    
class SizeCommandRepository:
    @staticmethod
    def create(size: str) -> Size:
        return Size.objects.create(
            size=size
        )

    @staticmethod
    def update_fast(id: int, **kwargs) -> int:
        return Size.objects.filter(
            id=id
        ).update(
            **kwargs
        )

    @staticmethod
    def update_safe(id: int, **kwargs) -> Size:
        obj = get_object_or_404(
            Size,
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