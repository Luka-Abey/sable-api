from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ShowSerializer
from .models import Show

class ScheduleView(APIView):
  def get(self, request, *args, **kwargs):
    data = {
      'name': 'sugar'
    }
    return Response(data)