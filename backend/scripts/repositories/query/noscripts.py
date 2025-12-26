from scripts.models import NoScripts
from scripts.repositories.base import BaseQueryRepository

class NoScriptsQueryRepository(BaseQueryRepository):
    model = NoScripts

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )