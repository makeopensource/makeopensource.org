from django.db import models
from django.forms import ModelForm, widgets
from datetime import date, datetime

YEAR = datetime.today().year
GRAD_YEAR = [(year, str(year)) for year in range(YEAR, YEAR + 6)]

class Member(models.Model):
	email = models.EmailField(primary_key=True, max_length=100)
	name = models.CharField(max_length=100)
	major = models.CharField(max_length=300)
	exp_grad_year = models.IntegerField(choices=GRAD_YEAR)
	join_date = models.DateField(default=date.today, editable=False)
	verified = models.BooleanField(default=False)

	def __str__(self):
		return self.name
