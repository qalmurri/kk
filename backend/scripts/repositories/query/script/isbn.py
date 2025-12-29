from scripts.models.script import Isbn, TypeIsbn
from scripts.repositories.query import BaseQueryRepository

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