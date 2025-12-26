from scripts.models import Cover
from scripts.repositories.base import BaseQueryRepository

class CoverBookQueryRepository(BaseQueryRepository):
    model = Cover

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )