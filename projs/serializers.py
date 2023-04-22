from rest_framework import serializers
from .models import Proj

class ProjSerializer(serializers.ModelSerializer):
  class Meta:
    model = Proj
    fields = (
      'id',
      'name',
      'banner',
      'chunk_one',
      'image_one',
      'chunk_two',
      'image_two',
      'chunk_three',
      'image_three',
      'chunk_four',
      'image_four',
      'chunk_five',
      'image_five',
      'chunk_six',
      'image_six',
      'author',
      'post_type',
      'date',
      )

class AllProjsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Proj
    fields = (
      'id',
      'name',
      'banner',
      'author',
      'post_type',
      'date'
      )
