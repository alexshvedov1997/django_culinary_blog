from rest_framework import serializers
from ..models import Category, CulinaryPost, Comment

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body','publish')

class CategorySeralizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','category_name', 'slug']

class CulinaryPostSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many = True)
    culinary_category = serializers.SlugRelatedField(slug_field="category_name", read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = CulinaryPost
        fields = ('id', 'title', 'author', 'publish', 'slug', 'culinary_category', 'comments')

class CulinaryPostAllFieldSerializers(serializers.ModelSerializer):

    class Meta:
        model = CulinaryPost
        fields = '__all__'