from scripts.models.script import Status, LabelStatus, SectionStatus
from scripts.repositories.query import BaseQueryRepository

class StatusQueryRepository(BaseQueryRepository):
    model = Status

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class SectionStatusQueryRepository(BaseQueryRepository):
    model = SectionStatus

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class LabelStatusQueryRepository(BaseQueryRepository):
    model = LabelStatus

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )