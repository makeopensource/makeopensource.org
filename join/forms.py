from django import forms

class JoinForm(forms.Form):
    name = forms.CharField(
		label='Name',
		max_length=100,
		widget=forms.TextInput(
			attrs={'type': 'text', 'class': 'form-control'}
		)
	)
    email = forms.EmailField(
		label='Email',
		max_length=100,
		widget=forms.EmailInput(
			attrs={'type': 'email', 'class': 'form-control'}
		)
	)
   
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
	
    year_in_school = forms.MultipleChoiceField(
		label='Year in college',
		choices=YEAR_IN_SCHOOL_CHOICES,
		widget=forms.Select(
			attrs={'class': 'form-select'}
		),
		required=True
	)

    major = forms.CharField(
		label='Major',
		max_length=100,
		widget=forms.TextInput(
			attrs={'type': 'text', 'class': 'form-control'}
		)
	)
