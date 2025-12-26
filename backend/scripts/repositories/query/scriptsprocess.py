from scripts.models import ScriptProcess, By, Section
from scripts.repositories.base import BaseQueryRepository

class ScriptsProcessQueryRepository(BaseQueryRepository):
    model = ScriptProcess

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class ByQueryRepository(BaseQueryRepository):
    model = By

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class SectionQueryRepository(BaseQueryRepository):
    model = Section

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )