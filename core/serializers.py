from rest_framework import serializers
from .models import Category


class FilterCategoryListSerializer(serializers.ListSerializer):
    """Only root categories on first level of input"""
    def to_representation(self, data):
        data = data.filter(parent_category=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Subcategories recursive output"""
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    """Categories list"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategoryListSerializer
        model = Category
        fields = ('name', 'children')
