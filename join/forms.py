from django import forms
from datetime import datetime
from .models import Member

YEAR = datetime.today().year
GRAD_YEAR = [(year, str(year)) for year in range(YEAR, YEAR + 6)]

class JoinForm(forms.Form):

    def is_unique(self) -> bool:
        return not Member.objects.filter(email=self.data['email']).exists()

    def unique_retval(self) -> str:
        if self.is_unique():
            return 'is-invalid'
        return 'is-valid'

    name = forms.CharField(
        required=True,
        label='Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',
                'placeholder': 'Name'
            }
        )
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'type': 'email', 
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )

    exp_grad_year = forms.IntegerField(
        required=True,
        label='Graduation Year',
        widget=forms.Select(
            choices=GRAD_YEAR,
            attrs={
                'class': 'form-select',
                'placeholder': 'Graduation Year'
            }
        )
    )

    major = forms.CharField(
        required=True,
        label='Major',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'type': 'text', 
                'class': 'form-control',
                'placeholder': 'Major'
            }
        )
    )