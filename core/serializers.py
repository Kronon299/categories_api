from rest_framework import serializers
from .models import Category


class RecursiveSerializer(serializers.Serializer):
    """Subcategories recursive output"""
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CategorySerializer(serializers.ModelSerializer):
    """Categories list"""
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'children')
