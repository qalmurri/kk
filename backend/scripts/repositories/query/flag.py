from scripts.models import Flag, SectionFlag
from scripts.repositories.base import BaseQueryRepository

class FlagQueryRepository(BaseQueryRepository):
    model = Flag

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class SectionFlagQueryRepository(BaseQueryRepository):
    model = SectionFlag

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )