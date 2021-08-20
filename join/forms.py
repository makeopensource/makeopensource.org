from django import forms
from datetime import datetime

from django.core.exceptions import ValidationError
from .models import Member


YEAR = datetime.today().year
GRAD_YEAR = [(year, str(year)) for year in range(YEAR, YEAR + 6)]


class JoinForm(forms.Form):

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.split()) > 1:
            return self.cleaned_data['name']
        else:
            self.add_error('name', 'Invalid Name')


    def clean_email(self):
        email = self.cleaned_data['email']
        if not Member.objects.filter(email=email).exists():
            return email
        else:
            self.add_error('email', 'An account was already registered with this email')


    name = forms.CharField(
        required=True,
        label='Full Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',
                'placeholder': 'Full Name'
            }))

    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type': 'email', 
                'class': 'form-control',
                'placeholder': 'alan@makeopensource.org'
            }))

    exp_grad_year = forms.IntegerField(
        required=True,
        label='Graduation Year',
        widget=forms.Select(
            choices=GRAD_YEAR,
            attrs={
                'class': 'form-select',
                'placeholder': 'Graduation Year'
            }))

    major = forms.CharField(
        required=True,
        label='Major',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',
                'placeholder': 'Computer Science'
            }))