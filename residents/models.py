from django.db import models

class Resident(models.Model):
  name = models.CharField(max_length=100, editable=True)
  description = models.CharField(max_length=1000, editable=True)
  image_url = models.CharField(max_length=100, editable=True)
  show_frequency = models.CharField(max_length=100, editable=True)
  mix_url_one = models.CharField(max_length=100, editable=True)
  mix_url_two = models.CharField(max_length=100, editable=True)
  mix_url_three = models.CharField(max_length=100, editable=True)

  def __str__(self):
    return self.name
