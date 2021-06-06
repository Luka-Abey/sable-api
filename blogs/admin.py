from django.contrib import admin
from .models import Blog
from django import forms

class BlogAdminForm(forms.ModelForm):
  class Meta:
    model = Blog
    widgets = {
      'chunk_one': {'size':'20'}
    }
    fields = '__all__'
    
class BlogAdmin(admin.ModelAdmin):
  form = BlogAdminForm

admin.site.register(Blog, BlogAdmin)
