from rest_framework import serializers
from .models import Show

class ResidentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Show
    fields = (
      'id',
      'name',
      'description',
      'image_url',
      'show_frequency',
      'mix_url_one',
      'mix_url_two',
      'mix_url_three')
