from django.db import models
from datetime import date

class Member(models.Model):
	name = models.CharField(primary_key=True, max_length=100)
	email = models.EmailField(max_length=100)
	major = models.CharField(max_length=300)
	join_date = models.DateField(default=date.today)

	# from django Models documentation #

	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	GRADUATE = 'GR'
	YEAR_IN_SCHOOL_CHOICES = [
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
		(GRADUATE, 'Graduate'),
	]
	year_in_school = models.CharField(
		max_length=2,
		choices=YEAR_IN_SCHOOL_CHOICES,
		blank=True,
	)

	###################################


	def __str__(self):
		return self.name
