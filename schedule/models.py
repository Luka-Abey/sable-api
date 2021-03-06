from django.db import models

class Show(models.Model):
  name = models.CharField(max_length=100, editable=True)
  date_time = models.DateTimeField(editable=True)
  end_time = models.DateTimeField(editable=True)
  live = models.BooleanField(default=True, editable=True)

  def __str__(self):
    start_time = self.date_time
    return f'{start_time.strftime("%d/%m/%Y")} - {self.name}'
