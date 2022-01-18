from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from .serializers import ShowSerializer
from .models import Show

class ScheduleView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Show.objects.all()
    serializer = ShowSerializer(qs, many=True)
    return Response(serializer.data)

class CurrentShowView(APIView):
  def get(self, request, *args, **kwargs):
    time_now = timezone.now()
    try:
      this_show = Show.objects.get(
        Q(date_time__lte=time_now) & Q(end_time__gt=time_now) 
      )
      serializer = ShowSerializer(this_show, many=False)
      return Response(serializer.data)
    
    except:
      return {}