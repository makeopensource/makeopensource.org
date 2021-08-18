from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Member
from .forms import JoinForm

from django.core.mail import send_mail



def index(request):
    
    if 'join_status' not in request.session:
        request.session['join_status'] = None

    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid() and form.is_unique():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            major = form.cleaned_data['major']
            exp_grad_year = form.cleaned_data['exp_grad_year']

            new_member = Member(email=email, name=name, major=major, exp_grad_year=exp_grad_year)
            new_member.save()
            request.session['join_status'] = 'joined'

            send_mail(
                subject='Thank you for joining MakeOpenSource',
                html_message='',
                from_email='from@example.com',
                recipient_list=['to@example.com'],
                fail_silently=False,
            )

            return HttpResponseRedirect('/join/')
        else:
            # return form with email error
            pass
    else:
        form = JoinForm()
    
    return render(request, 'join/index.html', 
        {'form': form, 'join_status': request.session['join_status']})
