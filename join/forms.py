from django import forms
import datetime
from django.utils import timezone

from .models import Member


YEAR: int = datetime.datetime.today().year
GRAD_YEAR = [(year, str(year)) for year in range(YEAR, YEAR + 6)]
# make sure this next line is what you think it should be, this broke the website, you cannot join a tuple and a string. - nick
GRAD_YEAR[-1] = GRAD_YEAR[-1], ' and beyond'
JOIN_EXPIRE = [datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(hours=24), datetime.datetime.now(tz=timezone.utc)]

class JoinForm(forms.Form):
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.split()) < 2:
            self.add_error('name', 'Invalid Name')
        return name
    
    def registered_email(self, email) -> bool:
        return Member.objects.filter(email=email, verified=False, join_date__range=JOIN_EXPIRE).exists() \
            or Member.objects.filter(email=email, verified=True).exists()

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email.split('@')) > 1 and email.split('@')[1] != 'buffalo.edu':
            self.add_error('email', 'Students must register with their @buffalo.edu email')
        elif self.registered_email(email):
            self.add_error('email', 'An account was already registered with this email')
        return email
    
    def clean_constitution(self):
        constitution = self.cleaned_data['constitution']
        if not constitution:
            self.add_error('constitution', 'Please agree to the constitution')
        return constitution

    name = forms.CharField(
        required=True,
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'type': 'text', 
                'class': 'form-control',
                'placeholder': 'Full Name',
                'div_css': 'form-floating'
            }),
    )

    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'type': 'email',
                'class': 'form-control',
                'placeholder': 'alan@makeopensource.org',
                'div_css': 'form-floating'
            }),
    )

    exp_grad_year = forms.IntegerField(
        required=True,
        label='Graduation Year',
        widget=forms.Select(
            choices=GRAD_YEAR,
            attrs={
                'id': 'grad_year',
                'class': 'form-select',
                'placeholder': 'Graduation Year',
                'div_css': 'form-floating'
            }),
    )

    major = forms.CharField(
        required=True,
        label='Major',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'id': 'major',
                'type': 'text', 
                'class': 'form-control',
                'placeholder': 'Computer Science',
                'div_css': 'form-floating'
            }),
    )
    
    notifications = forms.BooleanField(
        required=False,
        initial=True,
        label='Sign up for email announcements and notifications',
        widget=forms.CheckboxInput(
            attrs={
                'id': 'notifications',
                'class': 'form-check-input',
                'div_css': 'form-check'
            }),
    )

    constitution = forms.BooleanField(
        required=False,
        initial=False,
        label=  """I confirm that I have read and agree to 
                MakeOpenSource's Constitution and that I am 
                a student at the University at Buffalo""",
        widget=forms.CheckboxInput(
            attrs={
                'id': 'constitution',
                'class': 'form-check-input',
                'div_css': 'form-check'
            }),
    )
