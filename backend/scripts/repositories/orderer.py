from django.shortcuts import get_object_or_404
from scripts.models import Orderer

class OrdererQueryRepository:
    @staticmethod
    def list_all():
        return Orderer.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return Orderer.objects.get(
            id=id
        )
   
class OrdererCommandRepository:    
    @staticmethod
    def create(name: str, no: int) -> Orderer:
        return Orderer.objects.create(
            name=name,
            no=no
        )

    @staticmethod
    def update_fast(id: int, **kwargs) -> int:
        return Orderer.objects.filter(
            id=id
        ).update(
            **kwargs
        )

    @staticmethod
    def update_safe(id: int, **kwargs) -> Orderer:
        obj = get_object_or_404(
            Orderer,
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