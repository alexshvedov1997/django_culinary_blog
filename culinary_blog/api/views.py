from rest_framework import generics
from rest_framework.views import APIView
from  rest_framework.response import Response
from ..models import Category, CulinaryPost
from .serializers import CategorySeralizers, CulinaryPostSerializers, CulinaryPostAllFieldSerializers

class CreatePostView(generics.CreateAPIView):
    serializer_class = CulinaryPostAllFieldSerializers

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizers

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySeralizers

class PostListView(APIView):

    def get(self, request):
        post_list = CulinaryPost.objects.all()
        serializer = CulinaryPostSerializers(post_list, many=True)
        return  Response(serializer.data)
'''
    queryset = CulinaryPost.objects.all()
    serializer_class = CulinaryPostSerializers
'''

class PostDetailView(APIView):
    def get(self, request, pk):
        post_detail = CulinaryPost.objects.get(id = pk)
        serializer = CulinaryPostSerializers(post_detail)
        return Response(serializer.data)

class PostDetailViewGeneric(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CulinaryPostSerializers
    queryset = CulinaryPost.objects.all()


