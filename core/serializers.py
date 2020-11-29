from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    parent_category = serializers.CharField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

# class CategorySerializer(serializers.ModelSerializer):
#     parentCategory = serializers.PrimaryKeyRelatedField()
#     subcategories = SubCategorySerializer()
#
#     class Meta:
#         model = Category
#         fields = ('parentCategory', 'name', 'subcategories')