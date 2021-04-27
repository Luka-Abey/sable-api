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
    this_resident_id = self.kwargs['id']
    this_resident = Resident.objects.get(id=this_resident_id)
    serializer = ResidentSerializer(this_resident, many=False)
    return Response(serializer.data)

class SearchResidentsView(APIView):
  def get(self, request, *args, **kwargs):
    query_string = self.kwargs['search']
    filtered_residents = Resident.objects.filter(
      Q(name__icontains=query_string) |
      Q(description__icontains=query_string)
    )
    serializer = ResidentSerializer(filtered_residents, many=True)
    return Response(serializer.data)
