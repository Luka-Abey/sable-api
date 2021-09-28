from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime, timedelta

from .serializers import ResidentSerializer, AllResidentsSerializer
from .models import Resident

class ResidentsView(APIView):
  def get(self, request, *args, **kwargs):
    qs = Resident.objects.all()
    serializer = AllResidentsSerializer(qs, many=True)
    return Response(serializer.data)

class SingleResidentView(APIView):
  def get(self, request, *args, **kwargs):
    this_resident_name = ' '.join(self.kwargs['id'].split('-'))
    this_resident = Resident.objects.get(name=this_resident_name)
    serializer = ResidentSerializer(this_resident, many=False)
    return Response(serializer.data)

class SearchResidentsView(APIView):
  def get(self, request, *args, **kwargs):
    query_string = self.kwargs['search']
    filtered_residents = Resident.objects.filter(
      Q(name__icontains=query_string) |
      Q(description__icontains=query_string)
    )
    serializer = AllResidentsSerializer(filtered_residents, many=True)
    return Response(serializer.data)
