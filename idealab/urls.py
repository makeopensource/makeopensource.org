from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'idealab'

urlpatterns = [
    path('', views.index, name='index'),
    
    # API gateway for Idea objects
    path('ideas/', views.IdeaList.as_view()),
    path('ideas/<int:pk>/', views.IdeaDetail.as_view()),

    # API gateway for Author objects
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

# Authentication gateway
urlpatterns += [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
