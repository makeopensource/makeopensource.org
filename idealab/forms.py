from django import forms

class IdeaForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=200,
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control'}
        )
    )

    desc = forms.CharField(
        label='Description',
        max_length=1000,
        widget=forms.Textarea(
            attrs={'type': 'text', 'class': 'form-control', 'style': 'height: 200px; resize: none;'}
        )
    )

    authorname = forms.CharField(
        label='Author Name',
        max_length=200,
        widget=forms.TextInput(
            attrs={'type': 'text', 'class': 'form-control'}
        )
    )

    authoremail = forms.EmailField(
        label='Author Email',
        max_length=200,
        widget=forms.EmailInput(
            attrs={'type': 'email', 'class': 'form-control'}
        )
    )

