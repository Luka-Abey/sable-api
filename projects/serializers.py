from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
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

class AllProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = (
      'id',
      'name',
      'banner',
      'author',
      'post_type',
      'date'
      )
