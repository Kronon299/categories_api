from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})

    def post(self, request):
        categories = request.data.get('categories')
        # Create categories from the above data
        serializer = CategorySerializer(data=categories, partial=True)
        if serializer.is_valid(raise_exception=True):
            categories_saved = serializer.save()
        return Response({"success": f"Category '{categories_saved.name}' created successfully"})
