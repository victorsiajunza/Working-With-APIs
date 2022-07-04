from msilib.schema import ListView
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from links.models import Link
from .serializers import LinkSerializer
# Create your views here.
class PostListApi():
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    

class PostCreateApi():
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi():
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi():
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi():
    queryset= Link.objects.filter(active=True)
    serializer_class = LinkSerializer


