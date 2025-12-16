from scripts.models import CoverColor
    
class CoverColorQueryRepository:
    @staticmethod
    def list_all():
        return CoverColor.objects.all()
    
    @staticmethod
    def get_by_id(id: int):
        return CoverColor.objects.get(id=id)
   
class CoverColorCommandRepository:
    @staticmethod
    def create(color: str) -> CoverColor:
        return CoverColor.objects.create(
            color=color
        )

    @staticmethod
    def update(id: int, **kwargs):
        return CoverColor.objects.filter(id=id).update(**kwargs) 