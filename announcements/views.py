from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Announcement

from rest_framework.response import Response
from .serializers import AnnouncementSerializer
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend


# handles GET and POST requests for /announcements/
class AnnouncementList(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text', 'discord_id', 'created_at']


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
