from django.urls import path, include 
from rest_framework.urlpatterns import format_suffix_patterns 
from . import views
from rest_framework.authtoken import views as rf_views


app_name = 'announcements'

urlpatterns = [
    # API gateway for announcements
    path('', views.AnnouncementList.as_view()),
    path('<int:discord_id>/', views.AnnouncementDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

# token authentication framework
urlpatterns += [
    path('api-token-auth/', rf_views.obtain_auth_token)
]

