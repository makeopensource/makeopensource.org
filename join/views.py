from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import JoinForm
from .models import Member

def index(request):
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            major = form.cleaned_data['major']
            exp_grad_year = form.cleaned_data['exp_grad_year']
            print(name, email, major, exp_grad_year)
            b = Member(name=name, email=email, major=major, exp_grad_year=exp_grad_year)
            b.save()
            return HttpResponseRedirect('/join/')
    else:
        form = JoinForm()

    return render(request, 'join/index.html', {'form': form})
