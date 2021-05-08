from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BannerSerializer
from .models import Banner

class BannerView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Banner.objects.all()
    serializer = BannerSerializer(qs, many=True)
    return Response(serializer.data)