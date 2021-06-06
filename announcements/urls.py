from django.urls import path, include 
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views

app_name = 'announcements'

urlpatterns = [
    # API gateway for announcements
    path('', views.AnnouncementList.as_view()),
    path('<int:pk>/', views.AnnouncementDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Authentication gateway
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

