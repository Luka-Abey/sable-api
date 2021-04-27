from rest_framework import serializers
from .models import Resident

class ResidentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Resident
    fields = (
      'id',
      'name',
      'description',
      'image_url',
      'show_frequency',
      'mix_url_one',
      'mix_url_two',
      'mix_url_three',
      'soundcloud_url',
      'mixcloud_url',
      'facebook_url',
      'twitter_url',
      'instagram_url',
      'bandcamp_url',
      'youtube_url',
      )

class AllResidentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Resident
    fields = (
      'id',
      'name',
      'image_url',
      'show_frequency',
      )
