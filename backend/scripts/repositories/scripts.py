from django.db.models import Q
from scripts.models import Scripts
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsQueryRepository(BaseQueryRepository):
    model = Scripts

    @classmethod
    def get_queryset(cls):
        return (
            cls.model.objects
            .select_related("institute", "size")
            .prefetch_related(
                "scripts_ScriptsOrderer__orderer__institute",
                "scripts_Status",
                "scripts_Flag",
                "scripts_Description",
                "scripts_Note",
                "scripts_ISBN",
                "scripts_ScriptsProcess",
                "scripts_Cover",
            )
        )

    @classmethod
    def query(cls, params):
        qs = cls.get_queryset()

#        if "active" not in params:
#            qs = qs.filter(is_active=True)

        if params.get("active") in ("0", "1"):
            qs = qs.filter(
                is_active=bool(int(params["active"]))
            )

        if keyword := params.get("title"):
            qs = qs.filter(
                Q(title__icontains=keyword) |
                Q(alias__icontains=keyword)
            )

        return qs
    
class ScriptsCommandRepository(BaseCommandRepository):
    model = Scripts

    @classmethod
    def create(cls, **data) -> Scripts:
        return super().create(**data)

    @classmethod
    def update(cls, instance: Scripts, **data) -> Scripts:
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance