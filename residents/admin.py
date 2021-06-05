from django.contrib import admin
from django.db import models
from .models import Resident
from django import forms

class ResidentAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.CharField: {'widget': forms.Textarea}
  }

admin.site.register(Resident, ResidentAdmin)
