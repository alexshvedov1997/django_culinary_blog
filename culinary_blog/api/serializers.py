from rest_framework import serializers
from ..models import Category

class CategorySeralizers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','category_name', 'slug']