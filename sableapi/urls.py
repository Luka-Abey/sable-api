"""sableapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from schedule.views import ScheduleView, CurrentShowView
from residents.views import ResidentsView, SingleResidentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schedule', ScheduleView.as_view()),
    path('api/schedule/currentshow', CurrentShowView.as_view()),
    path('api/residents', ResidentsView.as_view()),
    # HERE NEED TO POINT TO SPECIFIC ID OR RESIDENT NAME
    # https://www.webforefront.com/django/accessurlparamstemplates.html
    path('api/residents/<int:id>', SingleResidentView.as_view()),
]
