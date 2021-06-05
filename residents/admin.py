from django.contrib import admin
from django.db import models
from .models import Resident

class ResidentAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
  }

admin.site.register(Resident, ResidentAdmin)
