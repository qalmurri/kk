from scripts.serializers.read import BaseReadSerializer
from rest_framework import serializers
from scripts.models.script import (
    Size,
    Institute
)

# jangan base, kalau ikut base maka create & update ikut tampil
class SizeReadSerializer(BaseReadSerializer):
    '''size read serializer'''
    class Meta(BaseReadSerializer.Meta):
        model = Size
        fields = BaseReadSerializer.Meta.fields + (
            "name",
        )

class InstituteReadSerializer(BaseReadSerializer):
    '''Institute read serializers'''
    class Meta(BaseReadSerializer.Meta):
        model = Institute
        fields = BaseReadSerializer.Meta.fields + (
                "name",
                )

# Kita pakai serializers, karena kalau pakai base yang isinya id, create & update akan bisa muncul saat GET
# Tetapi base memiliki kode lain untuk lazy load, jika memakai serializer, tidak bisa di lazy load. Harus mengambil fungsi lazy load

# class SizeReadSerializer(serializers.ModelSerializer):
#     '''size read serializer'''
#     class Meta():
#         model = Size
#         fields = (
#             "id",
#             "name",
#         )

# class InstituteReadSerializer(serializers.ModelSerializer):
#     '''institute read serializer'''
#     class Meta():
#         model = Institute
#         fields = (
#             "id",
#             "name",
#         )

