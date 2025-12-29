from django.shortcuts import get_object_or_404

class BaseQueryRepository:
    model = None

    @classmethod
    def get_queryset(cls):
        if cls.model is None:
            raise NotImplementedError(
                f"{cls.__name__}.model must be defined"
            )
        return cls.model.objects.all()

    @classmethod
    def get_by_id(cls, id: int):
        return get_object_or_404(
            cls.get_queryset(),
            id=id
        )