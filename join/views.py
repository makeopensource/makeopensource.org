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
            year_in_school = form.cleaned_data['year_in_school'][0]
            print(year_in_school)
            b = Member(name=name, email=email, major=major, year_in_school=year_in_school)
            print(b)
            b.save()
            return HttpResponseRedirect('/join/')
    else:
        form = JoinForm()

    return render(request, 'join/index.html', {'form': form})
