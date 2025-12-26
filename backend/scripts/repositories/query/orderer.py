from scripts.models import Orderer, ScriptsOrderer
from scripts.repositories.base import BaseQueryRepository

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