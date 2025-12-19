from django.shortcuts import get_object_or_404

class BaseQueryRepository:
    model = None

    @classmethod
    def list_all(cls):
        assert cls.model is not None, "model must be defined"
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, id: int):
        assert cls.model is not None, "model must be defined"
        return get_object_or_404(cls.model, id=id)

class BaseCommandRepository:
    model = None

    @classmethod
    def create(cls, **kwargs):
        assert cls.model is not None, "model must be defined"
        return cls.model.objects.create(**kwargs)

    @classmethod
    def update_fast(cls, id: int, **kwargs):
        assert cls.model is not None, "model must be defined"
        cls.model.objects.filter(id=id).update(**kwargs)

    @classmethod
    def soft_delete(cls, id: int):
        assert cls.model is not None, "model must be defined"
        cls.model.objects.filter(id=id).update(is_active=False)
