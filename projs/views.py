from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProjSerializer, AllProjsSerializer
from .models import Proj

def decode(url):
  decoded_url = url.replace("-", " ").replace("±", "-").replace("|", "/")
  return decoded_url

class ProjsView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Proj.objects.all()
    serializer = AllProjsSerializer(qs, many=True)
    return Response(serializer.data)

class SingleProjView(APIView):
  def get(self, request, *args, **kwargs):
    this_blog_name = decode(self.kwargs['id'])
    this_blog = Proj.objects.get(name=this_blog_name)
    serializer = ProjSerializer(this_blog, many=False)
    return Response(serializer.data)

class SearchProjsView(APIView):
  def get(self, request, *args, **kwargs):
    query_string = self.kwargs['search']
    filtered_blogs = Proj.objects.filter(
      Q(name__icontains=query_string) |
      Q(author__icontains=query_string)
    )
    serializer = AllProjsSerializer(filtered_blogs, many=True)
    return Response(serializer.data)
