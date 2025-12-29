from scripts.models.script import Size, Institute
from scripts.repositories.base import BaseQueryRepository

class SizeQueryRepository(BaseQueryRepository):
    model = Size

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class InstituteQueryRepository(BaseQueryRepository):
    model = Institute

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )