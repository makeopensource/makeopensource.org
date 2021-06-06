from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
        list_display = ['text', 'discord_id', 'created_at']
        ordering = ['created_at']

admin.site.register(Announcement, AnnouncementAdmin)
