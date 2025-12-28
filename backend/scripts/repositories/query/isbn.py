from scripts.models import Isbn, TypeIsbn
from scripts.repositories.base import BaseQueryRepository

class IsbnQueryRepository(BaseQueryRepository):
    model = Isbn

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class TypeIsbnQueryRepository(BaseQueryRepository):
    model = TypeIsbn

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )