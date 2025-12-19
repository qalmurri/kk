from django.db.models import Q
from django.shortcuts import get_object_or_404
from scripts.models import Scripts
from scripts.repositories.base import (
    BaseQueryRepository,
    BaseCommandRepository
)

class ScriptsQueryRepository(BaseQueryRepository):
    model = Scripts

    @classmethod
    def base_queryset(cls):
        return (
            cls.model.objects
            .select_related("institute", "size")
        )

    @classmethod
    def list_all(cls):
        return (
            cls.model.objects
            .all()
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
        qs = cls.base_queryset()

        if params.get("active") in ("0", "1"):
            qs = qs.filter(
                is_active=bool(int(params["active"]))
            )

        if keyword := params.get("title"):
            qs = qs.filter(
                Q(title__icontains=keyword) | Q(alias__icontains=keyword)
            )

        return qs

    @classmethod
    def get_by_id(cls, id: int) -> Scripts:
        return get_object_or_404(
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
            ),
            id=id
        )
    
class ScriptsCommandRepository(BaseCommandRepository):
    model = Scripts

    @classmethod
    def create(cls, **data) -> Scripts:
        """
        Create script utama.
        Relasi pivot / child bisa ditangani di service terpisah
        """
        return cls.model.objects.create(**data)

    @classmethod
    def update_fast(cls, id: int, **data) -> None:
        cls.model.objects.filter(id=id).update(**data)

    @classmethod
    def archive(cls, id: int) -> None:
        """
        Archive script (soft state change)
        """
        cls.model.objects.filter(id=id).update(
            is_active=False
        )

    @classmethod
    def restore(cls, id: int) -> None:
        cls.model.objects.filter(id=id).update(
            is_active=True
        )