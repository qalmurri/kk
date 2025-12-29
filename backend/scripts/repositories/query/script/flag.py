from scripts.models.script import Flag, SectionFlag
from scripts.repositories.query import BaseQueryRepository

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