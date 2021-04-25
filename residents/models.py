from django.db import models

class Resident(models.Model):
  name = models.CharField(max_length=100, editable=True)
  description = models.CharField(max_length=1000, editable=True)
  image_url = models.CharField(max_length=100, editable=True, blank=True)
  show_frequency = models.CharField(max_length=100, editable=True, blank=True)
  mix_url_one = models.CharField(max_length=100, editable=True, blank=True)
  mix_url_two = models.CharField(max_length=100, editable=True, blank=True)
  mix_url_three = models.CharField(max_length=100, editable=True, blank=True)
  soundcloud_url = models.CharField(max_length=100, editable=True, blank=True)
  mixcloud_url = models.CharField(max_length=100, editable=True, blank=True)
  facebook_url = models.CharField(max_length=100, editable=True, blank=True)
  twitter_url = models.CharField(max_length=100, editable=True, blank=True)
  instagram_url = models.CharField(max_length=100, editable=True, blank=True)
  bandcamp_url = models.CharField(max_length=100, editable=True, blank=True)
  youtube_url = models.CharField(max_length=100, editable=True, blank=True)

  def __str__(self):
    return self.name
