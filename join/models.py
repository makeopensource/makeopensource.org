from django.db import models
from datetime import date


class Member(models.Model):
	name = models.CharField(primary_key=True, max_length=100)
	email = models.EmailField(max_length=100)
	major = models.CharField(max_length=300)
	exp_grad_year = models.IntegerField()
	join_date = models.DateField(default=date.today, editable=False)

	def __str__(self):
		return self.name
