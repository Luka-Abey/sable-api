from django.db import models

class BannerPlus(models.Model):
  name = models.CharField(max_length=50, editable=True, blank=False)
  image_url = models.CharField(max_length=150, editable=True, blank=False)
  link_url = models.CharField(max_length=150, editable=True, blank=True)
  link_text = models.CharField(max_length=50, editable=True, blank=True)

  def __str__(self):
    return self.name
