"""mos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


handler404 = 'api.views.page_not_found'
handler500 = 'api.views.error'
handler400 = 'api.views.page_not_found'

urlpatterns = [
	path('', TemplateView.as_view(template_name='home/index.html')),
    path('api/', include('api.urls')),
	path('idealab/', include('idealab.urls')),
	path('projects/', include('projects.urls')),
	path('join/', include('join.urls')),
	path('about/', TemplateView.as_view(template_name='about/index.html')),
    path('calendar/', TemplateView.as_view(template_name='calendar/calendar.html')),
    path('announcements/', include('announcements.urls')),
    path('admin/', admin.site.urls),
    path('discord/', RedirectView.as_view(url='https://discord.gg/xbBPqdqr6n')),
    path('github/', RedirectView.as_view(url='https://github.com/makeopensource')),
]
