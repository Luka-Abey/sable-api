from django.contrib import admin
from django.db import models
from .models import Resident
from django import forms

class ResidentAdminForm(forms.ModelForm):
  class Meta:
    model = Resident
    widgets = {
      'description': forms.Textarea
    }
    fields = '__all__'
    
class ResidentAdmin(admin.ModelAdmin):
  form = ResidentAdminForm

admin.site.register(Resident, ResidentAdmin)
