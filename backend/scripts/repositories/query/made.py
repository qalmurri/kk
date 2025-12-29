from scripts.models.script import Made, ByMade, SectionMade
from scripts.repositories.base import BaseQueryRepository

class MadeQueryRepository(BaseQueryRepository):
    model = Made

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ByMadeQueryRepository(BaseQueryRepository):
    model = ByMade

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class SectionMadeQueryRepository(BaseQueryRepository):
    model = SectionMade

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )