from rest_framework import serializers
from blogsapp.models import Blog,Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    blogs=BlogSerializer(read_only=True,many=True)
    class Meta:
        model=Category
        fields="__all__"