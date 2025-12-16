from django.shortcuts import get_object_or_404
from scripts.models import Institute

class InstituteQueryRepository:
    @staticmethod
    def list_all():
        return Institute.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return Institute.objects.get(
            id=id
        )

class InstituteCommandRepository:
    @staticmethod
    def create(institute: str) -> Institute:
        return Institute.objects.create(
            institute=institute
        )

    @staticmethod
    def update_fast(id: int, **kwargs) -> int:
        return Institute.objects.filter(
            id=id
        ).update(
            **kwargs
        )

    @staticmethod
    def update_safe(id: int, **kwargs) -> Institute:
        obj = get_object_or_404(
            Institute,
            id=id
        )
        for key, value, in kwargs.items():
            setattr(
                obj,
                key,
                value
            )
        obj.save()
        return obj