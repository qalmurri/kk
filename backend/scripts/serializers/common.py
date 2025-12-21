from .base import PolicyBasedSerializer
from scripts.models import (
    Size,
    Orderer,
    Institute,
    ScriptsStatusCode,
    Label,
    Type,
    Part,
    DescriptionPart,
    NotePart,
    Section
)

# base
class BaseReadSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "id",
            "created_at",
            "updated_at",
        )

class BaseWriteSerializer(PolicyBasedSerializer):
    class Meta:
        abstract = True
        fields = (
            "name",
        )

# size
class SizeReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Size
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SizeWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Size

# institute
class InstituteReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Institute
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class InstituteWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Institute

# code
class CodeReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = ScriptsStatusCode
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class CodeWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = ScriptsStatusCode

# descriptionpart
class DescriptionPartReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = DescriptionPart
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class DescriptionPartWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = DescriptionPart

# labelread
class LabelReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Label
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class LabelWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Label

# notepart
class NotePartReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = NotePart
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class NotePartWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = NotePart

# part
class PartReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Part
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class PartWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Part

# section
class SectionReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Section
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class SectionWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Section

# type
class TypeReadSerializer(BaseReadSerializer):
    class Meta(BaseReadSerializer.Meta):
        model = Type
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class TypeWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Type

# orderer
class OrdererReadSerializer(BaseReadSerializer):
    institute = InstituteReadSerializer(
        read_only=True
    )

    class Meta(BaseReadSerializer.Meta):
        model = Orderer
        fields = BaseReadSerializer.Meta.fields + (
            "name",
            "no",
            "institute"
        )

class OrdererWriteSerializer(BaseWriteSerializer):
    class Meta(BaseWriteSerializer.Meta):
        model = Orderer
        fields = BaseWriteSerializer.Meta.fields + (
            "no",
            "institute",
        )