from scripts.models import Size

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