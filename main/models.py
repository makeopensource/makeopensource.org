from django.db import models

class Contributor(models.Model):

	name = models.CharField(max_length=100)

	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Project(models.Model):

	title = models.CharField(max_length=200)

	project_id = models.CharField('id', max_length = 8, unique=True)

	contributors = models.ManyToManyField(Contributor)

	github = models.CharField(max_length=200)
	
	description = models.TextField(max_length=1000)

	def __str__(self):
		return self.title
	

