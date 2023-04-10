from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProjectSerializer, AllProjectsSerializer
from .models import Project

def decode(url):
  decoded_url = url.replace("-", " ").replace("±", "-").replace("|", "/")
  return decoded_url

class ProjectsView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Project.objects.all()
    serializer = AllProjectsSerializer(qs, many=True)
    return Response(serializer.data)

class SingleProjectView(APIView):
  def get(self, request, *args, **kwargs):
    this_blog_name = decode(self.kwargs['id'])
    this_blog = Project.objects.get(name=this_blog_name)
    serializer = ProjectSerializer(this_blog, many=False)
    return Response(serializer.data)

class SearchProjectsView(APIView):
  def get(self, request, *args, **kwargs):
    query_string = self.kwargs['search']
    filtered_blogs = Project.objects.filter(
      Q(name__icontains=query_string) |
      Q(author__icontains=query_string)
    )
    serializer = AllProjectsSerializer(filtered_blogs, many=True)
    return Response(serializer.data)
