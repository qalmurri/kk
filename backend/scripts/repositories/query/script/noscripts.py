from scripts.models.script import NoScripts
from scripts.repositories.query import BaseQueryRepository

class NoScriptsQueryRepository(BaseQueryRepository):
    model = NoScripts

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )