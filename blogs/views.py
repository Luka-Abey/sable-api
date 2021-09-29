from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BlogSerializer, AllBlogsSerializer
from .models import Blog

def decode(url):
  decoded_url = url.replace("±", " ").replace("|", "/")
  return decoded_url

class BlogsView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Blog.objects.all()
    serializer = AllBlogsSerializer(qs, many=True)
    return Response(serializer.data)

class SingleBlogView(APIView):
  def get(self, request, *args, **kwargs):
    this_blog_name = decode(self.kwargs['id'])
    this_blog = Blog.objects.get(name=this_blog_name)
    serializer = BlogSerializer(this_blog, many=False)
    return Response(serializer.data)

class SearchBlogsView(APIView):
  def get(self, request, *args, **kwargs):
    query_string = self.kwargs['search']
    filtered_blogs = Blog.objects.filter(
      Q(name__icontains=query_string) |
      Q(author__icontains=query_string)
    )
    serializer = AllBlogsSerializer(filtered_blogs, many=True)
    return Response(serializer.data)
