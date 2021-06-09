from rest_framework import serializers
from .models import BannerPlus

class BannerPlusSerializer(serializers.ModelSerializer):
  class Meta:
    model = BannerPlus
    fields = ('id', 'name', 'image_url', 'link_url', 'link_text')
