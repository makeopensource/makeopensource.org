from django.db import models
from django.forms import ModelForm, widgets
from datetime import datetime

YEAR = datetime.today().year
GRAD_YEAR = [(year, str(year)) for year in range(YEAR, YEAR + 6)]

class Member(models.Model):
	email = models.EmailField(primary_key=True, max_length=100)
	name = models.CharField(max_length=100)
	major = models.CharField(max_length=300)
	exp_grad_year = models.IntegerField(choices=GRAD_YEAR)
	join_date = models.DateTimeField(default=datetime.today, editable=False)
	verified = models.BooleanField(default=False)
	notifications = models.BooleanField(default=True)

	def __str__(self):
		return self.name
