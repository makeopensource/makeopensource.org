from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'join'
urlpatterns = [
	path('', views.index, name='index'),
	path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
