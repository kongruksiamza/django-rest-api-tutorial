from blogsapp.models import Blog,Category
from blogsapp.serializer import BlogSerializer,CategorySerializer
from rest_framework import viewsets
from rest_framework import filters

class BlogViewset(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['id','title']


class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer