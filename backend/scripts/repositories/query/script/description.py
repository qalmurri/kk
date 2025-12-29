from scripts.models.script import Description, SectionDescription, TextDescription
from scripts.repositories.query import BaseQueryRepository

class DescriptionQueryRepository(BaseQueryRepository):
    model = Description

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )

class DescriptionPartQueryRepository(BaseQueryRepository):
    model = SectionDescription

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class TextQueryRepository(BaseQueryRepository):
    model = TextDescription

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )