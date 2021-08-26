from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rf_views

from idealab import views as idealab_views
from projects import views as project_views
from announcements import views as announcement_views

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    
    # API gateway for Ideas
    path('ideas/', idealab_views.IdeaList.as_view()),
    path('ideas/<int:pk>/', idealab_views.IdeaDetail.as_view()),

    # API gateway for Authors
    path('authors/', idealab_views.AuthorList.as_view()),
    path('authors/<int:pk>/', idealab_views.AuthorDetail.as_view()),

    # API gateway for Projects
    path('projects/', project_views.ProjectList.as_view()),
    path('projects/<int:pk>/', project_views.ProjectDetail.as_view()),

    # API gateway for Projects
    path('contributors/', project_views.ContributorList.as_view()),
    path('contributors/<int:pk>/', project_views.ContributorDetail.as_view()),

    # API gateway for Announcements
    path('announcements/', announcement_views.AnnouncementList.as_view()),
    path('announcements/<int:pk>/', announcement_views.AnnouncementDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# token authentication framework
urlpatterns += [
    path('api-token-auth/', rf_views.obtain_auth_token)
]

