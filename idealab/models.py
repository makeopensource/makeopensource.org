from django.db import models
import datetime

class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)

	def __str__(self):
		return self.name


class Idea(models.Model):
	title = models.CharField(max_length=200)
	release_date = models.DateField('date released', default=datetime.date.today)
	description = models.TextField(max_length=1000)
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
	approved = models.BooleanField('approval status', default=False)

	def __str__(self):
		return self.title

