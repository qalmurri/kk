from scripts.models import Purpose

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