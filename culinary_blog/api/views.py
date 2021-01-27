from rest_framework import generics
from ..models import Category
from .serializers import CategorySeralizers

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizers

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizers
