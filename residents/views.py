from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta

from .serializers import ResidentSerializer
from .models import Resident

class ResidentsView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Resident.objects.all()
    serializer = ResidentSerializer(qs, many=True)
    return Response(serializer.data)

class SingleResidentView(APIView):
  def get(self, request, *args, **kwargs):
    this_resident_name = request.query_params.get('name')
    this_resident = Resident.objects.filter(name=this_resident_name)
    serializer = ResidentSerializer(this_resident, many=False)
    return Response(serializer.data)
