from django.urls import path, include 
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views
from rest_framework.authtoken import views as rf_views


app_name = 'announcements'

urlpatterns = [
    # API gateway for announcements
    path('', views.index, name='index'),
]

