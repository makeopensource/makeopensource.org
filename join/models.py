from django.db import models

class Member(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	major = models.CharField(max_length=300)
	join_date = models.DateField(auto_now_add=True)


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
