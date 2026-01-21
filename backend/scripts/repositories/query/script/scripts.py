from django.db.models import Q
from scripts.models.script import Script
from scripts.repositories.query import BaseQueryRepository
from scripts.includes.script import SCRIPT_INCLUDES

class ScriptsQueryRepository(BaseQueryRepository):
    model = Script

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

# ORI    @classmethod
# ORI    def query(cls, params):
# ORI        qs = cls.get_queryset()
# ORI
# ORI#        if "active" not in params:
# ORI#            qs = qs.filter(is_active=True)
# ORI
# ORI        if params.get("active") in ("0", "1"):
# ORI            qs = qs.filter(
# ORI                is_active=bool(int(params["active"]))
# ORI            )
# ORI
# ORI        if keyword := params.get("title"):
# ORI            qs = qs.filter(
# ORI                Q(title__icontains=keyword) |
# ORI                Q(alias__icontains=keyword)
# ORI            )
# ORI
# ORI        return qs

    @classmethod
    def query(cls, params):
        view = params.get("view", "data")

        if view == "part":
            qs = cls.model.objects.select_related(
                "institute"
            )
        else:
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