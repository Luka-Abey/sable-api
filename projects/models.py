from django.db import models

class Project(models.Model):
  name          = models.CharField(max_length=100, editable=True)
  banner        = models.CharField(max_length=100, editable=True)
  chunk_one     = models.TextField(editable=True)
  image_one     = models.CharField(max_length=100, editable=True, blank=True)
  chunk_two     = models.TextField(editable=True, blank=True)
  image_two     = models.CharField(max_length=100, editable=True, blank=True)
  chunk_three   = models.TextField(editable=True, blank=True)
  image_three   = models.CharField(max_length=100, editable=True, blank=True)
  chunk_four    = models.TextField(editable=True, blank=True)
  image_four    = models.CharField(max_length=100, editable=True, blank=True)
  chunk_five    = models.TextField(editable=True, blank=True)
  image_five    = models.CharField(max_length=100, editable=True, blank=True)
  chunk_six     = models.TextField(editable=True, blank=True)
  image_six     = models.CharField(max_length=100, editable=True, blank=True)
  author        = models.CharField(max_length=100, editable=True, blank=True)
  post_type     = models.CharField(max_length=100, editable=True, blank=True)
  date          = models.CharField(max_length=100, editable=True, blank=True)
  
  def __str__(self):
    return f'{self.name} project'
