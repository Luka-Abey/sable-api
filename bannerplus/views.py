from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BannerPlusSerializer
from .models import BannerPlus

class BannerPlusView(APIView):
  def get(self, request, *args, **kwargs):
    qs = BannerPlus.objects.all()
    serializer = BannerPlusSerializer(qs, many=True)
    return Response(serializer.data)