from django.db import models

# annoucement model
class Announcement(models.Model):
    text = models.TextField(max_length=5000)
    discord_id = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.created_at

