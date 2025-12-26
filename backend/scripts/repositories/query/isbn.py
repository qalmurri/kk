from scripts.models import Isbn, Type
from scripts.repositories.base import BaseQueryRepository

class ISBNQueryRepository(BaseQueryRepository):
    model = Isbn

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class TypeQueryRepository(BaseQueryRepository):
    model = Type

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )