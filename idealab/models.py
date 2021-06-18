from django.db import models
import datetime


class Author(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField(max_length=200)
        github = models.CharField(max_length=200)
        def __str__(self):
                return self.name

# Open-Source project proposal
class Idea(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField('date released', default=datetime.date.today, editable=False)
    description = models.TextField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    approved = models.BooleanField('approval status', default=False)
    upvotes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


