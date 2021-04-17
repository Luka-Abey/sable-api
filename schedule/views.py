from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

from .serializers import ShowSerializer
from .models import Show

class ScheduleView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Show.objects.all()
    serializer = ShowSerializer(qs, many=True)
    return Response(serializer.data)

class CurrentShowView(APIView):
  def get(self, request, *args, **kwargs):
    time_now = datetime.now()
    this_show = Show.objects.get(
      Q(date_time <= time_now),
      Q(time_now < end_time ) 
    )
    serializer = ShowSerializer(this_show, many=False)
    return Response(serializer.data)
