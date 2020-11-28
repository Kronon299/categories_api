from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return Response({"categories": categories})
