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

class CodeSerializer(PolicyBasedSerializer):
    class Meta:
        model = ScriptsStatusCode
        fields = [
            "id",
            "name"
        ]

class DescriptionPartSerializer(PolicyBasedSerializer):
    class Meta:
        model = DescriptionPart
        fields = [
            "id",
            "name"
        ]

class InstituteSerializer(PolicyBasedSerializer):
    class Meta:
        model = Institute
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at"
        ]

class LabelSerializer(PolicyBasedSerializer):
    class Meta:
        model = Label
        fields = [
            "id",
            "name"
        ]

class NotePartSerializer(PolicyBasedSerializer):
    class Meta:
        model = NotePart
        fields = [
            "id",
            "name"
        ]

class PartSerializer(PolicyBasedSerializer):
    class Meta:
        model = Part
        fields = [
            "id",
            "name"
        ]

class SectionSerializer(PolicyBasedSerializer):
    class Meta:
        model = Section
        fields = [
            "id",
            "name"
        ]

class SizeSerializer(PolicyBasedSerializer):
    class Meta:
        model = Size
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at"
        ]

class TypeSerializer(PolicyBasedSerializer):
    class Meta:
        model = Type
        fields = [
            "id",
            "name"
        ]

class OrdererSerializer(PolicyBasedSerializer):
    institute = InstituteSerializer()

    class Meta:
        model = Orderer
        fields = [
            "id",
            "name",
            "no",
            "institute",
            "created_at",
            "updated_at"
        ]

class OrdererAllSerializer(PolicyBasedSerializer):
    class Meta:
        model = Orderer
        fields = [
            "id",
            "orderer",
            "no",
            "institute",
            "updated_at",
            "created_at"
        ]