from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Member
from .forms import JoinForm


def index(request):
    
    if 'join_status' not in request.session:
        request.session['join_status'] = None

    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            major = form.cleaned_data['major']
            exp_grad_year = form.cleaned_data['exp_grad_year']

            new_member = Member(email=email, name=name, major=major, exp_grad_year=exp_grad_year)
            new_member.save()
            request.session['join_status'] = 'joined'

            return HttpResponseRedirect('/join/')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = JoinForm()
    
    return render(request, 'join/index.html',
        {'form': form, 'join_status': request.session['join_status']})
