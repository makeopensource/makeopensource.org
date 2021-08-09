from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'idealab'

urlpatterns = [
    path('', views.index, name='index'),
]

