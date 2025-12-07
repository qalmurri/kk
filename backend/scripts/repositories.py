from .models import Purpose, Size, Institute, Orderer

class PurposeRepository:
    @staticmethod
    def create(code: int, purpose: str) -> Purpose:
        return Purpose.objects.create(
            code=code,
            purpose=purpose
        )

    @staticmethod
    def list_all():
        return Purpose.objects.all()
    
    @staticmethod
    def get_by_code(code: int):
        return Purpose.objects.filter(code=code)
    
    @staticmethod
    def get_by_id(id: int):
        return Purpose.objects.get(id=id)

    @staticmethod
    def update(id: int, **kwargs):
        return Purpose.objects.filter(id=id).update(**kwargs)
    
class SizeRepository:
    @staticmethod
    def create(size: str) -> Size:
        return Size.objects.create(
            size=size
        )

    @staticmethod
    def list_all():
        return Size.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return Size.objects.get(id=id)
    
    @staticmethod
    def update(id: int, **kwargs):
        return Size.objects.filter(id=id).update(**kwargs)

class InstituteRepository:
    @staticmethod
    def create(institute: str) -> Institute:
        return Institute.objects.create(
            institute=institute
        )

    @staticmethod
    def list_all():
        return Institute.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return Institute.objects.get(id=id)

    @staticmethod
    def update(id: int, **kwargs):
        return Institute.objects.filter(id=id).update(**kwargs)

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