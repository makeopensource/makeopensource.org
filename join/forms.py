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

    exp_grad_year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'min': '2021', 'max': '2026'}
        )
    )

    major = forms.CharField(
        label='Major',
        max_length=100,
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control'}
        )
    )

