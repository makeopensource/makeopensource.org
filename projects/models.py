from django.db import models

class Contributor(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=2000)
	contributors = models.ManyToManyField(Contributor)
	release_date = models.DateField(auto_now_add=True)
	github = models.CharField('github link', max_length=500)

	def __str__(self):
		return self.title
