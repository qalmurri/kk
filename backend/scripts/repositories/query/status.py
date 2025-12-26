from scripts.models import Status, LabelStatus, SectionStatus
from scripts.repositories.base import BaseQueryRepository

class StatusQueryRepository(BaseQueryRepository):
    model = Status

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ScriptsStatusCodeQueryRepository(BaseQueryRepository):
    model = SectionStatus

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class LabelQueryRepository(BaseQueryRepository):
    model = LabelStatus

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )