from scripts.models import Flag, Part
from scripts.repositories.base import BaseQueryRepository

class FlagQueryRepository(BaseQueryRepository):
    model = Flag

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class PartQueryRepository(BaseQueryRepository):
    model = Part

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )