from django.db import models

class Banner(models.Model):
  name = models.CharField(max_length=50, editable=True, blank=False)
  image_url = models.CharField(max_length=150, editable=True, blank=False)
  link_url = models.CharField(max_length=150, editable=True, blank=True)

  def __str__(self):
    return self.name
