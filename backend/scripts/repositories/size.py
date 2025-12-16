from scripts.models import Size
from django.shortcuts import get_object_or_404

class SizeQueryRepository:
    @staticmethod
    def list_all():
        return Size.objects.all()
    
    @staticmethod
    def get_by_id(id: int) -> Size:
        return get_object_or_404(Size, id=id)
    
class SizeCommandRepository:
    @staticmethod
    def create(size: str) -> Size:
        return Size.objects.create(
            size=size
        )
    
    @staticmethod
    def update(id: int, **kwargs) -> Size:
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