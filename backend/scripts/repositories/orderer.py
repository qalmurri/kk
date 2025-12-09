from scripts.models import Orderer

class OrdererRepository:
    @staticmethod
    def create(orderer: str, no: int) -> Orderer:
        return Orderer.objects.create(
            orderer=orderer,
            no=no
        )

    @staticmethod
    def list_all():
        return Orderer.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return Orderer.objects.get(id=id)
    
    @staticmethod
    def update(id: int, **kwargs):
        return Orderer.objects.filter(id=id).update(**kwargs)