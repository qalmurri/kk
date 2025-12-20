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

class BaseCommandRepository:
    model = None

    @classmethod
    def _check_model(cls):
        if cls.model is None:
            raise NotImplementedError(
                f"{cls.__name__}.model must be defined"
            )

    @classmethod
    def create(cls, **data):
        cls._check_model()
        return cls.model.objects.create(**data)

    @classmethod
    def update(cls, instance, **data):
        cls._check_model()
        for field, value in data.items():
            setattr(
                instance,
                field,
                value
            )
        instance.save()
        return instance
    
    @classmethod
    def archive(cls, instance, *, field="is_active"):
        cls._check_model()
        setattr(
            instance,
            field,
            False
        )
        instance.save(
            update_fields=[field]
        )
        return instance

    @classmethod
    def restore(cls, instance, *, field="is_active"):
        cls._check_model()
        setattr(
            instance,
            field,
            True
        )
        instance.save(
            update_fields=[field]
        )
        return instance

    @classmethod
    def hard_delete(cls, instance):
        cls._check_model()
        instance.delete()