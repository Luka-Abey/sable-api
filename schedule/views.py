from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ShowSerializer
from .models import Show

class ScheduleView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Show.objects.all()
    serializer = ShowSerializer(qs, many=True)
    return Response(serializer.data)
