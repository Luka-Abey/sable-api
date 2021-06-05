from django.contrib import admin
from django.db import models
from .models import Resident

class ResidentAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.CharField: {'widget': Resident.description(attrs={'size':'20'})},
    models.CharField: {'widget': Resident.mix_url_one(attrs={'rows':4, 'cols':40})},
  }

admin.site.register(Resident, ResidentAdmin)
