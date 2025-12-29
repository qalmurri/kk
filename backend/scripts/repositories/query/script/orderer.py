from scripts.models.script import Orderer, ScriptsOrderer
from scripts.repositories.query import BaseQueryRepository

class OrdererQueryRepository(BaseQueryRepository):
    model = Orderer

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )
    
class ScriptsOrdererQueryRepository(BaseQueryRepository):
    model = ScriptsOrderer

    @classmethod
    def query(cls):
        return (
            cls.model.objects
        )