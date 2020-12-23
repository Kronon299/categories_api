from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategoriesSerializer, CategorySerializer


class CategoriesView(APIView):
    """Categories list output"""
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        categories = request.data.get('categories')
        # Create categories from the above data
        serializer = CategoriesSerializer(data=categories, partial=True)
        if serializer.is_valid(raise_exception=True):
            categories_saved = serializer.save()
        return Response({"success": f"Category '{categories_saved.name}' created successfully"})


class CategoryDetailView(APIView):
    """Category detail output"""
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
